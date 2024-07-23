# Oppie : Ransomware Scanner
[![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)](https://opensource.org/licenses/Apache-2.0)
![VirusTotal](https://img.shields.io/badge/VirusTotal-Integrated-green)
## Table of Contents
1. [Description](#description)
2. [Usage](#usage)
3. [Key Features](#key-features)
4. [Installation](#installation)
5. [License](#license)
6. [Contact](#contact)

## Description
**Oppie** is a sophisticated ransomware scanner hosted on a Flask server, offering four layers of protection: real-time scanning with Python Watchdog for immediate threat detection, custom scanning using Yara rules for tailored threat identification, deep scanning based on hash values for thorough examination, and URL scanning via the VirusTotal API to ensure safe web interactions. This multi-faceted approach ensures comprehensive security against ransomware threats.
## Installation

1. **Install Python**: Ensure you have Python 3.6 or higher installed on your system.

2. **Install Required Packages**: Install the necessary Python packages using pip. You can do this with the following command in your Terminal:

    ```bash
    pip install flask colorama
    ```
3. **Disable Anti-Virus**: Temporarily disable any anti-virus services to ensure uninterrupted scanning.

