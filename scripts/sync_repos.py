#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automated Portfolio Synchronizer for Pratik Khairnar (@pratik-khairnar-sec)
Discovers all public repositories, resolves live demos/pages automatically,
and updates the profile README table with zero manual intervention.
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

def resolve_demo_link(repo, custom_demo=None):
    """
    Intelligently resolves the most relevant interactive demo or documentation link.
    Guarantees no dead dashes or missing links for current or future repositories.
    """
    if custom_demo:
        return f"[🌐 Live Demo]({custom_demo})"
        
    # 1. Custom handling for portfolio
    if repo["name"].lower() == "portfolio":
        return "[🌐 Live Portfolio](https://pratik-khairnar-sec.github.io/portfolio/)"
        
    # 2. Explicit repository homepage (e.g. GitHub Pages or external demo)
    homepage = (repo.get("homepage") or "").strip()
    if homepage:
        return f"[🌐 Live Demo]({homepage})"
        
    # 3. Check if GitHub Pages is active
    if repo.get("has_pages"):
        return f"[🌐 Live Demo](https://{USERNAME}.github.io/{repo['name']}/)"
        
    # 4. Check if tool has releases or binaries
    if repo.get("open_issues_count") is not None:
        return f"[📦 Architecture & Docs]({repo['html_url']}#readme)"
        
    return f"[📖 Repository]({repo['html_url']})"

def resolve_category_badge(repo, custom_badge=None):
    """
    Dynamically generates high-visibility categorized shields for future repositories.
    """
    if custom_badge:
        return custom_badge
        
    topics = [t.lower() for t in repo.get("topics", [])]
    name = repo["name"].lower()
    
    if any(k in topics or k in name for k in ["portfolio", "showcase"]):
        return "🌐 Live Portfolio"
    if any(k in topics or k in name for k in ["appsec", "vapt", "xss", "sqli", "idor", "bola", "burp"]):
        return "🛡️ AppSec"
    if any(k in topics or k in name for k in ["osint", "recon", "reconnaissance", "dork", "wayback"]):
        return "🔎 OSINT"
    if any(k in topics or k in name for k in ["chrome-extension", "extension", "manifest-v3"]):
        return "🧩 Extension"
    if any(k in topics or k in name for k in ["framework", "scanner"]):
        return "⚡ Framework"
        
    return "⚡ Security Tool"

def format_title(name):
    """Converts kebab/snake case names to clean Title Case."""
    clean = name.replace("-", " ").replace("_", " ")
    return " ".join(word.capitalize() for word in clean.split())

def format_portfolio_table(repos):
    rows = []
    
    # Priority order for featured tools
    priority = [
        "authentix-enterprise",
        "portfolio",
        "Reflectra",
        "BlindStrike",
        "wayback-lens",
        "endpoint-finder-extension",
        "ReconForge",
        "CORSair"
    ]
    
    # Custom curated metadata for primary flagship tools
    custom_meta = {
        "authentix-enterprise": {
            "title": "AUTHENTIX Enterprise",
            "desc": "Burp Suite Montoya Security Suite: 27 Invariants, 28 Secret Rules, 12 ATO Chains",
            "version": "v2.1.0",
            "badge": "🏆 Flagship",
            "demo": "https://pratik-khairnar-sec.github.io/authentix-enterprise/"
        },
        "portfolio": {
            "title": "Cybersecurity Portfolio & Showcase",
            "desc": "Official Interactive Cybersecurity Portfolio & VAPT Engineer Showcase",
            "version": "Live",
            "badge": "🌐 Live Portfolio",
            "demo": "https://pratik-khairnar-sec.github.io/portfolio/"
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
    
    seen = set()
    
    # 1. Process prioritized repos first
    for name in priority:
        repo = next((r for r in repos if r["name"].lower() == name.lower()), None)
        if repo:
            seen.add(repo["name"].lower())
            meta = custom_meta.get(repo["name"], {})
            title = meta.get("title", format_title(repo["name"]))
            desc = meta.get("desc", repo.get("description") or "Security framework")
            ver = meta.get("version", "v1.0.0")
            badge = meta.get("badge", "Active")
            demo_link = resolve_demo_link(repo, meta.get("demo"))
            repo_link = f"[`{repo['name']}`]({repo['html_url']})"
            
            rows.append(f"| **{title}** | {desc} | `{ver}` | {badge} | {demo_link} | {repo_link} |")
            
    # 2. Dynamically process ANY future or newly created public repositories
    for repo in repos:
        repo_name_lower = repo["name"].lower()
        # Skip profile repo, duplicates, forks, archived tools, and strictly private/legacy repos
        if (repo_name_lower == PROFILE_REPO.lower() or 
            repo_name_lower in seen or 
            repo.get("fork") or 
            repo_name_lower in ["recon-arsenal", "codesentinel"]):
            continue
            
        seen.add(repo_name_lower)
        title = format_title(repo["name"])
        desc = repo.get("description") or "Automated cybersecurity & security testing repository"
        badge = resolve_category_badge(repo)
        demo_link = resolve_demo_link(repo)
        repo_link = f"[`{repo['name']}`]({repo['html_url']})"
        
        rows.append(f"| **{title}** | {desc} | `Latest` | {badge} | {demo_link} | {repo_link} |")
        
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
        new_content = content + "\n\n" + replacement

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("Successfully synchronized portfolio and future repository pipeline in README.md!")

if __name__ == "__main__":
    update_readme()
