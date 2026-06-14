# mini-port-scanner


A command-line TCP port scanner that checks open ports on a target IP address or hostname and identifies running services using Python's socket module.

Built for learning basic networking concepts, port scanning techniques, and cybersecurity reconnaissance fundamentals.

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Category](https://img.shields.io/badge/category-Networking-green)

---

## Features

* Scan IP addresses or hostnames
* Custom port range selection
* Detect open TCP ports
* Identify common services (HTTP, SSH, HTTPS, etc.)
* Display real-time scan results
* Show scan duration and summary
* Automatically generate scan report file

---

## Requirements

```bash
python 3.x
```

No external libraries are required.

---

## Usage

```bash
python scanner.py
```

```text
========================================
MINI PORT SCANNER
========================================

Enter IP Address or Hostname: scanme.nmap.org
Start Port: 20
End Port: 100
```

---

## How it works

1. The user provides a target IP address or hostname
2. The hostname is resolved into an IP address (if needed)
3. The scanner attempts TCP connections on each port in the selected range
4. Open ports are identified using socket connection success
5. Common services are mapped to known ports
6. Results are displayed in the terminal
7. A scan report is saved automatically

---

## Example Output

```text
[OPEN] Port 22    Service: ssh
[OPEN] Port 80    Service: http
```

```text
SCAN SUMMARY
Open Ports Found: 2
Scan Duration: 1.34 seconds
```

---

## Project Structure

```text
mini-port-scanner/

├── scanner.py
├── README.md
├── .gitignore
└── results.txt (auto-generated)
```

---

## Learning Outcomes

* Python networking fundamentals
* Socket programming
* TCP port scanning logic
* DNS resolution concepts
* Error handling in network applications
* Basic cybersecurity reconnaissance techniques

---

## ⚠️ Important

* This tool is intended for educational and learning purposes only.
* Do not use it to scan systems without permission.
* Only test on authorized or local environments.
