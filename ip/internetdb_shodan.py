import sys
import requests as rq
import json


def get_ip_info(ip):
    url = f"https://internetdb.shodan.io/{ip}"
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


content = []

if len(result["hostnames"]) > 0:
    content.append({"## Hostnames": result["hostnames"]})

if len(result["ports"]) > 0:
    content.append({"## Ports": result["ports"]})

if len(result["cpes"]) > 0:
    content.append({"## CPEs": result["cpes"]})

if len(result["tags"]) > 0:
    content.append({"## Tags": result["tags"]})

if len(result["cpes"]) > 0:
    content.append({"## CPEs": result["cpes"]})

if len(result["vulns"]) > 0:
    content.append({"## Vulns": result["vulns"]})


print(
    json.dumps(
        {
            "type": "Tree",
            "results": content,
        }
    )
)
