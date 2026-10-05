<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,1,2,3,4&customColorList=0:#030712,1:#06b6d4,2:#10b981,3:#030712&height=210&section=header&text=Pratik%20Khairnar&fontSize=42&fontColor=ffffff&fontAlignY=42&desc=Cyber%20Security%20Researcher%20%E2%80%A2%20Security%20Tool%20Developer%20%E2%80%A2%20AppSec%20%2F%20VAPT&descAlignY=62&descSize=18&descColor=38bdf8" width="100%" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=20&pause=1000&color=38BDF8&center=true&vCenter=true&width=750&lines=Cyber+Security+Researcher+%26+Security+Tool+Developer;Creator+of+AUTHENTIX%2C+ReconArsenal%2C+Reflectra+%26+BlindStrike;AppSec+%2F+VAPT+Specialist+%E2%80%A2+Burp+Suite+Montoya+API;Engineering+Zero-False-Positive+Security+Engines;Defensive+Security+%26+Bug+Bounty+Research" alt="Typing SVG" />
</p>

<p align="center">
  <a href="https://github.com/pratik-khairnar-sec"><img src="https://img.shields.io/badge/Security%20Researcher-AppSec%20%7C%20VAPT-10b981?style=for-the-badge&logo=shield&logoColor=white" alt="Researcher"></a>
  <a href="https://github.com/pratik-khairnar-sec"><img src="https://img.shields.io/badge/Frameworks-8%20Specialized%20Suites-38bdf8?style=for-the-badge&logo=github&logoColor=white" alt="Tools"></a>
  <a href="https://github.com/pratik-khairnar-sec"><img src="https://img.shields.io/badge/Focus-Burp%20Extensions%20%7C%20OSINT-a855f7?style=for-the-badge&logo=target" alt="Focus"></a>
  <a href="#-strict-ethical-disclosure-statement"><img src="https://img.shields.io/badge/Research-Defensive%20Only-f59e0b?style=for-the-badge&logo=warning" alt="Ethical"></a>
</p>

---

## ⚡ About Me

I am a **Cyber Security Researcher**, **Application Security (AppSec) Analyst**, and **Security Tool Developer** from India. 

My primary mission is engineering high-speed, zero-false-positive security verification frameworks that replace noisy, outdated scanners with surgical precision. Every tool I publish features clean architectures, zero unnecessary dependencies, automated Telegram alerting, and dedicated interactive web triage environments.

- 🛡️ **Core Domains**: Web Application Penetration Testing (VAPT), Burp Suite Extension Development (Montoya API), OSINT Attack Surface Discovery, Blind SQLi Detection, Context-Aware XSS Analysis, and Chrome Extension Security Tooling.
- 🎯 **Philosophy**: Strict mathematical baselining, empirical latency calibration, headless browser confirmation, and defensive research.

---

## 🏆 Flagship Security Framework: AUTHENTIX v2.1.0

> **Next-Generation Authentication, IDOR/BOLA & Secret Scanner Security Suite for Burp Suite**
> *(Built on native PortSwigger Montoya API • Java 17/21 • Deterministic Finite-State Automaton)*

`
       [ Burp Suite HTTP Proxy / Repeater / Scanner / Intruder ]
                                   │
                                   ▼
                       [ TrafficInterpreter.java ]
                 (Actor Attribution & Flow Classification)
                                   │
         ┌─────────────────────────┴─────────────────────────┐
         ▼                                                   ▼
[ FlowGraphEngine.java ]                        [ TokenLifecycleTracker.java ]
(Per-Actor State Machine)                     (SHA-256 Hashes, Shannon Entropy,
                                                Single-Use, Expiration, JWT)
         │                                                   │
         └─────────────────────────┬─────────────────────────┘
                                   ▼
         ┌─────────────────────────┴─────────────────────────┐
         ▼                                                   ▼
[ InvariantEngine.java ]                        [ FileAnalyzerEngine.java ]
 (27 Formal Invariants)                          (28 Secret / Logic Rules)
         │                                                   │
         └─────────────────────────┬─────────────────────────┘
                                   ▼
                      [ AttackPathCorrelator.java ]
               (Chains Findings into 12 Compound ATO Graphs)
                                   │
         ┌─────────────────────────┴─────────────────────────┐
         ▼                                                   ▼
[ Burp Suite Modern UI Tabs ]                       [ Telegram Alerts Push ]
  - Findings & Cross-Actor Matrix                     - Zero UI Latency Async
  - Attack Chains Graph Studio                        - Kali cURL PoC Generator
`

### ⚡ AUTHENTIX Core Capabilities:
- 🎯 **Cross-Actor IDOR & BOLA Matrix**: Auto-detects sequential/UUID IDs and maps horizontal & vertical privilege escalation.
- 🛡️ **27 Formal Security Invariants**: Deterministic state machine checks covering OTP replay, session fixation, token entropy, JWT structural flaws, and BFLA.
- 🔬 **28 Deep Secret Analysis Rules**: Scans HTTP streams for JWT secrets, AWS, GCP, Azure, OpenAI, Claude, GitHub, Stripe, Firebase, Telegram, and SendGrid keys.
- ⛓️ **12 Correlated Attack Chain Rules**: Synthesizes compound findings into Account Takeover (ATO) kill-chain graphs.
- 📱 **Telegram Bot Dispatcher**: Mobile alerts with terminal-ready Kali cURL reproduction commands in real time.
- 🏦 **NimbusBank v2 Lab**: 16 banking challenge vectors with automated exploit verification.

---

## 🛡️ Complete Security Arsenal Portfolio

| Framework / Tool | Core Functionality | Version | Status / Access | Interactive Demo | Repository |
|---|---|---|---|---|---|
| **AUTHENTIX** | Burp Suite Montoya Security Suite: 27 Invariants, 28 Secret Rules, 12 ATO Chains | 2.1.0 | 🔒 Private Enterprise | Spotlight Above | [AUTHENTIX](https://github.com/pratik-khairnar-sec/AUTHENTIX) *(Private)* |
| **[ReconArsenal](https://github.com/pratik-khairnar-sec/recon-arsenal)** | Unified OSINT & Passive Threat Surface Suite (Wayback CDX, AlienVault OTX, Passive DNS, Punycode, Dorks) | 1.0.0 | 🌐 Public | [🌐 Live Demo](https://pratik-khairnar-sec.github.io/recon-arsenal/) | [econ-arsenal](https://github.com/pratik-khairnar-sec/recon-arsenal) |
| **[Reflectra](https://github.com/pratik-khairnar-sec/Reflectra)** | Context-aware XSS verification engine with Headless Chrome confirmation & DOM-sink analysis | 7.0.0 | 🌐 Public | [🌐 Live Demo](https://pratik-khairnar-sec.github.io/Reflectra/) | [Reflectra](https://github.com/pratik-khairnar-sec/Reflectra) |
| **[BlindStrike](https://github.com/pratik-khairnar-sec/BlindStrike)** | Time-Based & Boolean Blind SQLi framework with baseline latency calibration & jitter normalization | 7.0.0 | 🌐 Public | [🌐 Live Demo](https://pratik-khairnar-sec.github.io/BlindStrike/) | [BlindStrike](https://github.com/pratik-khairnar-sec/BlindStrike) |
| **[WaybackLens](https://github.com/pratik-khairnar-sec/wayback-lens)** | High-Performance Wayback Machine CDX Recon & Triage Workspace Chrome Extension (Manifest V3) | 1.0.0 | 🌐 Public | [🌐 Live Demo](https://pratik-khairnar-sec.github.io/wayback-lens/) | [wayback-lens](https://github.com/pratik-khairnar-sec/wayback-lens) |
| **[EndpointFinder](https://github.com/pratik-khairnar-sec/endpoint-finder-extension)** | Autonomous Manifest V3 Chrome Extension for client-side JS endpoint, API route, and parameter harvesting | 1.0.0 | 🌐 Public | [🌐 Live Demo](https://pratik-khairnar-sec.github.io/endpoint-finder-extension/) | [endpoint-finder-extension](https://github.com/pratik-khairnar-sec/endpoint-finder-extension) |
| **[ReconForge](https://github.com/pratik-khairnar-sec/ReconForge)** | Master Bug Bounty & VAPT Multi-Target Reconnaissance Framework with 33 Master Phases & 13,600+ Dorks | 3.0.0 | 🌐 Public | [🌐 Live Demo](https://pratik-khairnar-sec.github.io/ReconForge/) | [ReconForge](https://github.com/pratik-khairnar-sec/ReconForge) |
| **[CORSair](https://github.com/pratik-khairnar-sec/CORSair)** | Cross-Origin Request Security Analysis & PoC Engine with automated exploitation staging | 3.0.0 | 🌐 Public | [🌐 Live Demo](https://pratik-khairnar-sec.github.io/CORSair/) | [CORSair](https://github.com/pratik-khairnar-sec/CORSair) |

---

## 📊 Live GitHub Telemetry

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=pratik-khairnar-sec&show_icons=true&theme=tokyonight&hide_border=true&bg_color=050811&title_color=38bdf8&text_color=94a3b8&icon_color=10b981" alt="GitHub Stats" width="49%" />
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=pratik-khairnar-sec&theme=tokyonight&hide_border=true&background=050811&ring=38bdf8&fire=10b981&currStreakLabel=10b981" alt="GitHub Streak" width="49%" />
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=pratik-khairnar-sec&layout=compact&theme=tokyonight&hide_border=true&bg_color=050811&title_color=38bdf8&text_color=94a3b8" alt="Top Languages" width="60%" />
</p>

---

## 🛠️ Technical Competencies & Security Stack

<p align="center">
  <img src="https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white" alt="Java">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white" alt="Bash">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Burp%20Suite-FF6633?style=for-the-badge&logo=burp-suite&logoColor=white" alt="Burp">
  <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux">
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git">
  <img src="https://img.shields.io/badge/OWASP-000000?style=for-the-badge&logo=owasp&logoColor=white" alt="OWASP">
</p>

- **Security Disciplines**: Burp Suite Montoya API Extension Architecture, Web Application Pentesting (OWASP Top 10), Time-Based/Boolean Blind SQLi Detection, Cross-Site Scripting (XSS), Cross-Origin Resource Sharing (CORS), Open-Source Intelligence (OSINT).
- **Chrome Extension Security**: Manifest V3 DevTools Protocols, Client-Side JavaScript AST Crawling, Content Script Isolation.
- **Automation & Telemetry**: Multi-threaded concurrency, Telegram Bot API dispatching, Zero-dependency CLI tooling.

---

## 🛡️ Strict Ethical Disclosure Statement

> [!IMPORTANT]
> All software, scripts, and research published under this account are developed strictly for **educational security research**, **authorized penetration testing**, and **defensive vulnerability assessments**. 
> 
> Testing against targets without explicit, prior written authorization from the system owner is strictly prohibited and illegal. As a researcher, I adhere strictly to responsible disclosure practices and ethical security standards.

---

<p align="center">
  <b>Designed &amp; Maintained by Pratik Khairnar</b><br>
  <sub>⚡ Securing Applications • Engineering High-Velocity Defensive Frameworks ⚡</sub>
</p>