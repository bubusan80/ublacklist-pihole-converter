import requests
from urllib.parse import urlparse

UBLACKLIST_URL = "https://raw.githubusercontent.com/uBlacklist/blocked/main/uBlacklist.txt"

response = requests.get(UBLACKLIST_URL)
lines = response.text.splitlines()

domains = set()
for line in lines:
    line = line.strip()
    if not line or line.startswith("!"):
        continue

    # Rimuove protocollo e wildcard
    line = line.replace("*://", "").replace("http://", "").replace("https://", "")
    line = line.split("/")[0]  # Rimuove path

    # Estrae dominio valido
    parsed = urlparse("http://" + line)
    hostname = parsed.hostname
    if hostname and "." in hostname:
        domains.add(hostname.lower())

with open("pihole_blocklist.txt", "w", encoding="utf-8") as f:
    for domain in sorted(domains):
        f.write(domain + "\n")
