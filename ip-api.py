import sys
import requests as rq
import json


def get_ip_info(ip):
    url = f"http://ip-api.com/json/{ip}"
    return rq.get(url)


resp = get_ip_info(sys.argv[1])
result = {}

if resp.status_code == 200:
    result = resp.json()
elif resp.status_code == 404:
    print(
        json.dumps(
            {
                "type": "Tree",
                "results": ["No information available"],
            }
        )
    )
    exit()


print(
    json.dumps(
        {
            "type": "Tree",
            "results": [
                f"### Country\n{result['country']}\n---\n### Region Name\n{result['regionName']}\n---\n### City\n{result['city']}\n---\n### Org\n{result['org']}\n---\n### AS\n{result['as']}\n---"
            ],
        }
    )
)
