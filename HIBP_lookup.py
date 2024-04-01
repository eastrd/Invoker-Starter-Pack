API_KEY = ""


import sys
import requests as rq
import json


def get_breach_info(email, api_key):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {"hibp-api-key": api_key, "user-agent": "breach-checker"}
    try:
        response = rq.get(url, headers=headers)
        if response.status_code == 200:
            return response.json(), ""
        response.raise_for_status()
    except rq.exceptions.RequestException as e:
        return None, str(e)


result, err = get_breach_info(sys.argv[1], API_KEY)

if err:
    print(json.dumps({"type": "Tree", "results": [f"# Error\n{err}"]}))
else:
    domains = []
    for each in result:
        domains.append(f"### {each['Name']}")

    print(
        json.dumps(
            {
                "type": "Tree",
                "results": domains,
            }
        )
    )
