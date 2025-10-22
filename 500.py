#!/usr/bin/env python3
"""
organized_site_code.py
Fetch and display a website's HTML, CSS, and JavaScript in order:
1️⃣ HTML
2️⃣ CSS
3️⃣ JavaScript

Optimized for Pydroid 3 — easy to copy and read.
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# ====== SETTINGS ======
MAX_CHARS_PER_SECTION = 100000  # Prevent huge spam
INCLUDE_EXTERNAL = True  # Fetch CDN assets (True/False)
# =======================

def get_input(prompt, default=None):
    val = input(prompt).strip()
    return val if val else default

def make_session(proxy=None):
    s = requests.Session()
    s.headers.update({"User-Agent": "PydroidSiteViewer/1.0"})
    if proxy:
        s.proxies = {"http": proxy, "https": proxy}
    return s

def same_origin(a, b):
    pa, pb = urlparse(a), urlparse(b)
    return (pa.scheme, pa.netloc) == (pb.scheme, pb.netloc)

def fetch_text(session, url):
    try:
        r = session.get(url, timeout=20)
        r.raise_for_status()
        return r.text
    except Exception as e:
        return f"/* Failed to fetch {url} — {e} */"

def fetch_assets(session, urls, base_url, label, include_external=True):
    combined = ""
    seen = set()
    for u in urls:
        if not u or u in seen:
            continue
        seen.add(u)
        if not include_external and not same_origin(u, base_url):
            continue
        code = fetch_text(session, u)
        combined += f"\n/* --- {label.upper()} FILE: {u} --- */\n{code}\n"
    return combined

def main():
    print("=== Organized Site Code Viewer ===")
    url = get_input("Enter target URL: ")
    proxy = get_input("Enter proxy (or press Enter for none): ")

    session = make_session(proxy)
    print("\nFetching main HTML...\n")
    html = fetch_text(session, url)
    soup = BeautifulSoup(html, "html.parser")

    # --- Extract inline and linked assets ---
    inline_css = [tag.string or "" for tag in soup.find_all("style")]
    linked_css = [urljoin(url, link["href"]) for link in soup.find_all("link", href=True)
                  if "stylesheet" in (link.get("rel") or []) or link["href"].endswith(".css")]

    inline_js = [tag.string or "" for tag in soup.find_all("script") if not tag.has_attr("src")]
    linked_js = [urljoin(url, s["src"]) for s in soup.find_all("script", src=True)]

    # --- Fetch linked assets ---
    print("Fetching linked CSS and JS files...\n")
    css_code = fetch_assets(session, linked_css, url, "css", INCLUDE_EXTERNAL)
    js_code = fetch_assets(session, linked_js, url, "js", INCLUDE_EXTERNAL)

    # --- Combine all organized sections ---
    combined_output = []
    combined_output.append("/* ====== PAGE HTML ====== */\n" + html[:MAX_CHARS_PER_SECTION])

    if inline_css or css_code.strip():
        all_css = "\n".join(inline_css) + "\n" + css_code
        combined_output.append("\n/* ====== PAGE CSS ====== */\n" + all_css[:MAX_CHARS_PER_SECTION])

    if inline_js or js_code.strip():
        all_js = "\n".join(inline_js) + "\n" + js_code
        combined_output.append("\n/* ====== PAGE JAVASCRIPT ====== */\n" + all_js[:MAX_CHARS_PER_SECTION])

    print("\n\n=== ORGANIZED SITE CODE OUTPUT ===\n")
    print("\n\n".join(combined_output))

    print("\n=== END OF OUTPUT ===")

if __name__ == "__main__":
    main()