import requests
from urllib.parse import urlparse

URL = "https://raw.githubusercontent.com/popcar2/BadWebsiteBlocklist/refs/heads/main/uBlacklist.txt"

response = requests.get(URL)
lines = response.text.splitlines()

domains = set()
for line in lines:
    line = line.strip()
    if not line or line.startswith("!") or not "*://" in line:
        continue

    # Rimuove protocollo e path
    line = line.replace("*://", "").split("/")[0]
    line = line.lstrip("*.")  # Rimuove wildcard iniziale

    parsed = urlparse("http://" + line)
    hostname = parsed.hostname
    if hostname and "." in hostname:
        domains.add(hostname.lower())

with open("pihole_blocklist.txt", "w", encoding="utf-8") as f:
    for domain in sorted(domains):
        f.write(domain + "\n")
