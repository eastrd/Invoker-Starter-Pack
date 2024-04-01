import requests as rq
import sys
import json


def get_crtsh(domain):
    res = rq.get(f"https://crt.sh/?q={domain}&output=json")
    j = res.json()
    records = []
    for item in j:
        common_name = item["common_name"].lower()
        name_values = map(lambda x: x.lower(), item["name_value"].split("\n"))
        records.extend(name_values)
        records.append(common_name)

    records = list(set(records))  # dedup

    subdomains = []
    emails = []
    for subdomain in records:
        subdomain = subdomain.replace("*.", "")
        if subdomain == domain:
            continue
        if "@" in subdomain:
            emails.append(subdomain)
        else:
            subdomains.append(subdomain)

    return subdomains, emails


results = get_crtsh(sys.argv[1])
sub_domains = results[0]
emails = results[1]

results = []

for sub_domain in sub_domains:
    results.append(f"### {sub_domain}")

print(
    json.dumps(
        {
            "type": "Tree",
            "results": results,
        }
    )
)
