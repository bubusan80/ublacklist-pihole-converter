import requests
import re

# URL della lista uBlacklist (modificabile)
UBLACKLIST_URL = "https://raw.githubusercontent.com/uBlacklist/blocked/main/uBlacklist.txt"

response = requests.get(UBLACKLIST_URL)
lines = response.text.splitlines()

domains = set()
for line in lines:
    if line.startswith("!") or not line.strip():
        continue
    cleaned = line.strip().lower()
    if "." in cleaned:
        domains.add(cleaned)

with open("pihole_blocklist.txt", "w", encoding="utf-8") as f:
    for domain in sorted(domains):
        f.write(domain + "\n")
