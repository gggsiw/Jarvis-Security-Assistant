# Jarvis Security Assistant

Voice-controlled cybersecurity assistant built with Python that can execute security tools using natural voice commands.

## Features

- 🎙️ Wake phrase support (`Hello Jarvis`)
- 🗣️ Speech recognition
- 🔊 Voice responses
- 🌐 Supports URL/IP/domain targets
- 🔎 Aggressive Nmap scanning
- 🕷️ Nikto integration
- 🧩 Gobuster integration
- 📡 DNS lookups
- 🔍 Subfinder integration
- 🏹 Assetfinder integration
- ⚡ Nuclei integration
- 🐞 Bug Bounty Mode
- 📁 Automatic result output

---

## Demo

Example interaction:

```text
You: Hello Jarvis

Jarvis: Hello. How can I assist you today?

You: Aggressive scan

Jarvis:
Starting aggressive Nmap scan...
```

---

## Architecture

```text
Microphone
      ↓
Speech Recognition
      ↓
Jarvis (Python)
      ↓
Security Tool Execution
      ↓
Results
```

---

## Installation

### Clone repository

```bash
git clone https://github.com/gggsiw/Jarvis-Security-Assistant.git

cd Jarvis-Security-Assistant
```

### Create virtual environment

Windows:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### Install Python packages

```bash
pip install -r requirements.txt
```

---

## Python Requirements

requirements.txt

```txt
SpeechRecognition
pyttsx3
pyaudio
```

Install manually if needed:

```bash
pip install SpeechRecognition pyttsx3 pyaudio
```

---

## Install Security Tools

Make sure these tools are installed and available in PATH:

- Nmap
- Nikto
- Gobuster
- Subfinder
- Assetfinder
- Nuclei
- SQLMap
- Dirb
- Dig

You can verify installation:

```powershell
Get-Command nmap
Get-Command nuclei
Get-Command subfinder
```

---

## Running Jarvis

```bash
python jarvis.py
```

You will see:

```text
Target URL/IP/domain:
```

Enter:

```text
demo.testfire.net
```

---

## Supported Voice Commands

### Assistant

```text
Hello Jarvis
Goodbye Jarvis
```

### Scanning

```text
Aggressive

web scan

Find subdomains

asset discovery

run nuclei

Run gobuster

DNS lookup
```

### Modes

```text
Normal mode

Bug bounty mode
```

---

## Bug Bounty Mode

Bug bounty mode performs a broader workflow:

```text
Subfinder
↓
Assetfinder
↓
Nmap
↓
Nuclei
↓
Parameter collection
↓
Additional recon
```

Note:

This mode can take several minutes depending on target size.

---

## Project Structure

```text
Jarvis-Security-Assistant/
│
├── jarvis.py
├── requirements.txt
├── README.md
├── LICENSE
```

---

## Future Improvements

- AI investigation layer
- Session memory
- Dashboard UI
- Automatic report generation
- Screenshot mode
- Parallel scans
- Findings summarization

---

## Disclaimer

This tool is intended for educational purposes and authorized security testing only.

Only test systems you own or have permission to assess.

---

## License

MIT License
