# 🔍 Subdomain Scanner

A simple Python tool to find subdomains using a wordlist.

## 🛠️ How It Works
- Reads a list of subdomain names from a wordlist file
- Combines each one with a domain (e.g., `admin.example.com`)
- Sends an HTTP request to check if it exists

## 🧪 Example Usage

```bash
python subdomain_scanner.py example.com wordlist.txt
