import requests as rq
import sys
import json
from bs4 import BeautifulSoup as bs


def get_whois(domain):
    url = f"https://www.whois.com/whois/{domain}"
    res = rq.get(url)
    soup = bs(res.content, "html.parser")
    # Extract raw WHOIS data
    rows = soup.find_all("div", class_="df-row")
    return "\n".join(row.text.strip() for row in rows)


domain = sys.argv[1]
whois_info = get_whois(domain)

print(
    json.dumps(
        {
            "type": "Tree",
            "results": [f"```\n{whois_info}\n```"],
        }
    )
)
