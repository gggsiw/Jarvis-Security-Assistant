# Jarvis Security Assistant

Voice-controlled cybersecurity assistant that integrates security tools through Kali Linux and WSL.

## Features

- Wake phrase support: `Hello Jarvis`
- Voice recognition
- Nmap integration
- Nikto integration
- Subfinder
- Assetfinder
- Nuclei
- Gobuster
- DNS lookup
- Bug bounty mode
- Report saving

## Architecture

Windows Microphone
↓
Python Voice Layer
↓
WSL/Kali
↓
Security Tools

## Installation

Clone repository:

```bash
git clone https://github.com/gggsiw/Jarvis-Security-Assistant.git
cd Jarvis-Security-Assistant
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Install required Kali tools:

```bash
sudo apt install nmap nikto gobuster dirb dnsutils
```

## Usage

Run:

```bash
python jarvis.py
```

Examples:

```text
Hello Jarvis
Aggressive scan
Find subdomains
DNS lookup
Bug bounty mode
```

## Future Plans

- AI investigation layer
- Dashboard
- Report generation
- Session memory
- Screenshot mode
