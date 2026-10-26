"""
Technical SEO, Broken Link, Schema.org & Security Auditor — Python Quickstart
Official Apify Store Actor: https://apify.com/lucacelli/seo-technical-audit-broken-link-schema-analyzer ($0.80 / 1,000 pages)
"""
import os
import requests

APIFY_TOKEN = os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
ENDPOINT = "https://api.apify.com/v2/acts/lucacelli~seo-technical-audit-broken-link-schema-analyzer/run-sync-get-dataset-items"

payload = {
    "urls": [
        "https://apify.com",
        "https://cloudflare.com"
    ],
    "checkBrokenLinks": True
}

if __name__ == "__main__":
    print(f"Running Technical SEO, Broken Link, Schema.org & Security Auditor on Apify Cloud ({ENDPOINT})...")
    response = requests.post(f"{ENDPOINT}?token={APIFY_TOKEN}", json=payload, timeout=300)
    response.raise_for_status()
    data = response.json()
    print(f"Extracted {len(data)} records! Sample:")
    print(data[:3])
