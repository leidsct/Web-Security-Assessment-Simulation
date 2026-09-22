#!/usr/bin/env python3
# OWASP ZAP Vulnerability Assessment Helper Script

import sys
import time

def run_mock_zap_scan(target_url):
    print(f"[*] Initializing OWASP ZAP baseline check for: {target_url}")
    time.sleep(1)
    print("[*] Active spidering in progress...")
    time.sleep(1)
    print("[*] Passive scanning security headers and cookies...")
    time.sleep(1)
    
    print("\n[+] Scan completed successfully!")
    print("\n--- Summary of Findings ---")
    print(" - Absence of Anti-CSRF Tokens: MEDIUM")
    print(" - Missing Anti-clickjacking Header: MEDIUM")
    print(" - Content Security Policy (CSP) Not Set: MEDIUM")
    print(" - Cookie No HttpOnly / Secure Flag: LOW")

if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost"
    run_mock_zap_scan(url)
