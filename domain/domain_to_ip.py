import socket
import sys
import json


def get_ip_from_domain(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        return "Error: Unable to resolve domain: " + str(domain)


ip = get_ip_from_domain(sys.argv[1])

print(
    json.dumps(
        {
            "type": "Tree",
            "results": [f"## {ip}"],
        }
    )
)
