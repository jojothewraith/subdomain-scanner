import requests
import sys

def scan_subdomains(domain, wordlist):
    print(f"Scanning {domain} for subdomains...\n")
    with open(wordlist, "r") as file:
        for line in file:
            sub = line.strip()
            url = f"http://{sub}.{domain}"
            try:
                response = requests.get(url, timeout=2)
                print(f"[+] Found: {url}")
            except requests.ConnectionError:
                pass

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python subdomain_scanner.py <domain> <wordlist.txt>")
        sys.exit(1)

    domain = sys.argv[1]
    wordlist = sys.argv[2]
    scan_subdomains(domain, wordlist)
