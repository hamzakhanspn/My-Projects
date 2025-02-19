import requests
from bs4 import BeautifulSoup

def scan_security_headers(target_domain):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(f"https://{target_domain}", headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            security_headers = {
                "X-Frame-Options": "X-Frame-Options",
                "X-XSS-Protection": "X-XSS-Protection",
                "X-Content-Type-Options": "X-Content-Type-Options",
                "Content-Security-Policy": "Content-Security-Policy",
                "Expect-CT": "Expect-CT",
                "Strict-Transport-Security": "Strict-Transport-Security",
                "Permissions-Policy": "Permissions-Policy",
                "Referrer-Policy": "Referrer-Policy",
            }

            for header, key in security_headers.items():
                if key in response.headers:
                    print(f"[+] {header} found: {response.headers[key]}")
                else:
                    print(f"[-] {header} not found")
        else:
            print(f"[-] Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[-] Error: {e}")

# Example usage
target_domain = "app.quicksite.guru"  # Replace with the target domain
scan_security_headers(target_domain)
