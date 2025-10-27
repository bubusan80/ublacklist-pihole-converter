import requests
import re

# URL della lista uBlacklist (modificabile)
UBLACKLIST_URL = "https://raw.githubusercontent.com/gorhill/uBlacklist/master/assets/blocklist.txt"

# Scarica la lista
response = requests.get(UBLACKLIST_URL)
lines = response.text.splitlines()

# Estrai i domini
domains = set()
for line in lines:
    if line.startswith("!") or not line.strip():
        continue
    match = re.search(r"([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})", line)
    if match:
        domains.add(match.group(1).lower())

# Salva in formato Pi-hole
with open("pihole_blocklist.txt", "w", encoding="utf-8") as f:
    for domain in sorted(domains):
        f.write(domain + "\n")
