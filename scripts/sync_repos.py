#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automated Portfolio Synchronizer for Pratik Khairnar (@pratik-khairnar-sec)
Discovers all public repositories and updates the profile README table automatically.
"""

import urllib.request
import json
import re
import os

USERNAME = "pratik-khairnar-sec"
PROFILE_REPO = "pratik-khairnar-sec"

def fetch_repos():
    url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100&type=owner&sort=updated"
    req = urllib.request.Request(url, headers={"User-Agent": "Portfolio-Sync"})
    token = os.getenv("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
        
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"Error fetching repos: {e}")
        return []

def format_portfolio_table(repos):
    rows = []
    
    # Priority order for featured tools
    priority = [
        "authentix-enterprise",
        "recon-arsenal",
        "Reflectra",
        "BlindStrike",
        "wayback-lens",
        "endpoint-finder-extension",
        "ReconForge",
        "CORSair"
    ]
    
    # Custom display metadata
    custom_meta = {
        "authentix-enterprise": {
            "title": "AUTHENTIX Enterprise",
            "desc": "Burp Suite Montoya Security Suite: 27 Invariants, 28 Secret Rules, 12 ATO Chains",
            "version": "v2.1.0",
            "badge": "🏆 Flagship",
            "demo": "https://pratik-khairnar-sec.github.io/authentix-enterprise/"
        },
        "recon-arsenal": {
            "title": "ReconArsenal",
            "desc": "Unified OSINT & Passive Threat Surface Suite (Wayback CDX, OTX, Passive DNS, Dorks)",
            "version": "v1.0.0",
            "badge": "⚡ Core Suite",
            "demo": "https://pratik-khairnar-sec.github.io/recon-arsenal/"
        },
        "Reflectra": {
            "title": "Reflectra",
            "desc": "Context-aware XSS scanner with Headless Chrome verification & DOM-sink analysis",
            "version": "v7.0.0",
            "badge": "🛡️ AppSec",
            "demo": "https://pratik-khairnar-sec.github.io/Reflectra/"
        },
        "BlindStrike": {
            "title": "BlindStrike",
            "desc": "Time-Based & Boolean Blind SQLi framework with baseline latency calibration",
            "version": "v7.0.0",
            "badge": "🛡️ AppSec",
            "demo": "https://pratik-khairnar-sec.github.io/BlindStrike/"
        },
        "wayback-lens": {
            "title": "WaybackLens",
            "desc": "High-Performance Wayback Machine CDX Recon & Triage Chrome Extension (Manifest V3)",
            "version": "v1.0.0",
            "badge": "🔎 OSINT",
            "demo": "https://pratik-khairnar-sec.github.io/wayback-lens/"
        },
        "endpoint-finder-extension": {
            "title": "EndpointFinder",
            "desc": "Autonomous Chrome Extension for deep client-side JS endpoint & parameter extraction",
            "version": "v1.0.0",
            "badge": "🔎 Recon",
            "demo": "https://pratik-khairnar-sec.github.io/endpoint-finder-extension/"
        },
        "ReconForge": {
            "title": "ReconForge",
            "desc": "Master Bug Bounty & VAPT Multi-Target Framework with 33 Phases & 13,600+ Dorks",
            "version": "v3.0.0",
            "badge": "⚡ Framework",
            "demo": "https://pratik-khairnar-sec.github.io/ReconForge/"
        },
        "CORSair": {
            "title": "CORSair",
            "desc": "Cross-Origin Request Security Analysis & PoC Engine with automated exploitation staging",
            "version": "v3.0.0",
            "badge": "🛡️ AppSec",
            "demo": "https://pratik-khairnar-sec.github.io/CORSair/"
        }
    }
    
    # Process prioritized repos first
    seen = set()
    for name in priority:
        repo = next((r for r in repos if r["name"].lower() == name.lower()), None)
        if repo:
            seen.add(repo["name"])
            meta = custom_meta.get(repo["name"], {})
            title = meta.get("title", repo["name"])
            desc = meta.get("desc", repo.get("description") or "Security framework")
            ver = meta.get("version", "v1.0.0")
            badge = meta.get("badge", "Active")
            demo_url = meta.get("demo") or repo.get("homepage")
            demo_link = f"[🌐 Live Demo]({demo_url})" if demo_url else "—"
            repo_link = f"[`{repo['name']}`]({repo['html_url']})"
            
            rows.append(f"| **{title}** | {desc} | `{ver}` | {badge} | {demo_link} | {repo_link} |")
            
    # Process any other public repositories dynamically (future repos!)
    for repo in repos:
        if repo["name"] == PROFILE_REPO or repo["name"] in seen or repo.get("fork"):
            continue
        seen.add(repo["name"])
        desc = repo.get("description") or "Security research repository"
        demo_url = repo.get("homepage")
        demo_link = f"[🌐 Live Demo]({demo_url})" if demo_url else "—"
        repo_link = f"[`{repo['name']}`]({repo['html_url']})"
        rows.append(f"| **{repo['name']}** | {desc} | `Latest` | 🚀 Dynamic | {demo_link} | {repo_link} |")
        
    header = [
        "| Framework / Tool | Core Functionality | Version | Category | Interactive Demo | Repository |",
        "|---|---|---|---|---|---|"
    ]
    return "\n".join(header + rows)

def update_readme():
    repos = fetch_repos()
    if not repos:
        print("No repositories retrieved.")
        return

    table_md = format_portfolio_table(repos)
    readme_path = "README.md"
    
    if not os.path.isfile(readme_path):
        print("README.md not found.")
        return

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = r"<!-- START_PORTFOLIO -->.*?<!-- END_PORTFOLIO -->"
    replacement = f"<!-- START_PORTFOLIO -->\n{table_md}\n<!-- END_PORTFOLIO -->"
    
    if re.search(pattern, content, re.DOTALL):
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    else:
        # Fallback if markers are missing
        new_content = content + "\n\n" + replacement

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("Successfully synchronized portfolio in README.md!")

if __name__ == "__main__":
    update_readme()
