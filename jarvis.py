import speech_recognition as sr
import pyttsx3
import subprocess
import os
from urllib.parse import urlparse
from datetime import datetime



engine = pyttsx3.init()
engine.setProperty("rate",175)

def speak(text):
    print(f"\nJarvis: {text}")
    engine.say(text)
    engine.runAndWait()



raw_target=input("Target URL/IP/domain: ").strip()

def clean_target(target):
    if target.startswith(("http://","https://")):
        return urlparse(target).netloc
    return target

host=clean_target(raw_target)

timestamp=datetime.now().strftime("%Y%m%d_%H%M%S")

report_dir=f"reports/{host}_{timestamp}"

os.makedirs(report_dir,exist_ok=True)



COMMANDS={

"aggressive":
["wsl.exe","nmap","-A",host],

"web scan":
["wsl.exe","nikto","-h",raw_target],

"find subdomains":
["wsl.exe","subfinder","-d",host],

"asset discovery":
["wsl.exe","assetfinder","--subs-only",host],

"run nuclei":
["wsl.exe","nuclei","-u",raw_target],

"dns lookup":
["wsl.exe","dig",host],

"gobuster scan":
[
"wsl.exe",
"gobuster",
"dir",
"-u",
raw_target,
"-w",
"/usr/share/wordlists/dirb/common.txt"
]
}



def run_and_save(command,filename):

    try:

        result=subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        filepath=f"{report_dir}/{filename}"

        with open(filepath,"w",encoding="utf-8") as f:
            f.write(result.stdout)

        return result.stdout

    except Exception as e:
        return str(e)




def bug_bounty_mode():

    speak("Starting bug bounty mode")

    tasks=[

    (
    ["wsl.exe","subfinder","-d",host],
    "subfinder.txt"
    ),

    (
    ["wsl.exe","assetfinder","--subs-only",host],
    "assetfinder.txt"
    ),

    (
    ["wsl.exe","httpx","-u",host],
    "alive.txt"
    ),

    (
    ["wsl.exe","naabu","-host",host],
    "ports.txt"
    ),

    (
    ["wsl.exe","katana","-u",raw_target],
    "crawl.txt"
    ),

    (
    ["wsl.exe","paramspider","-d",host],
    "params.txt"
    ),

    (
    ["wsl.exe","nuclei","-u",raw_target],
    "nuclei.txt"
    ),

    (
    [
    "wsl.exe",
    "gobuster",
    "dir",
    "-u",
    raw_target,
    "-w",
    "/usr/share/wordlists/dirb/common.txt"
    ],
    "gobuster.txt"
    )

    ]

    for cmd,file in tasks:

        speak(f"Running {file}")

        run_and_save(cmd,file)

    speak("Bug bounty mode complete")

    summary=f"""
Target: {host}

Saved reports:
{report_dir}

Completed:
Subfinder
Assetfinder
HTTPX
Naabu
Katana
Paramspider
Nuclei
Gobuster
"""

    print(summary)



recognizer=sr.Recognizer()

speak("Jarvis online")

while True:

    try:

        with sr.Microphone() as source:

            print("\nListening...")

            recognizer.adjust_for_ambient_noise(
            source,
            duration=1
            )

            audio=recognizer.listen(
            source
            )

            text=recognizer.recognize_google(
            audio
            ).lower()

            print("\nYou:",text)

            if "hello jarvis" in text:

                speak(
                "Hello. How can I assist you today?"
                )

            elif "bug bounty" in text:

                bug_bounty_mode()

            elif "goodbye" in text or "good bye" in text:

                speak("Goodbye")
                break

            else:

                for cmd in COMMANDS:

                    if cmd in text:

                        speak(f"Running {cmd}")

                        subprocess.run(
                        COMMANDS[cmd]
                        )

                        break

    except Exception:
        pass