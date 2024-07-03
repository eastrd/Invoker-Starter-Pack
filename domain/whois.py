import requests as rq
import sys
import json
from bs4 import BeautifulSoup as bs

def get_whois(domain):
    url = f"https://www.whois.com/whois/{domain}"
    res = rq.get(url)
    soup = bs(res.content, 'html.parser')
    # Extract raw WHOIS data
    raw_data = soup.find('pre', class_='df-raw')
    return raw_data.text.strip()


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
