# Oppie : Ransomware Scanner
[![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)](https://opensource.org/licenses/Apache-2.0)

## Table of Contents
1. [Description](#description)
2. [Key Features](#key-features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [License](#license)
6. [Contact](#contact)

## Description
**Oppie** is a sophisticated ransomware scanner hosted on a Flask server, offering four layers of protection: real-time scanning with Python Watchdog for immediate threat detection, custom scanning using Yara rules for tailored threat identification, deep scanning based on hash values for thorough examination, and URL scanning via the VirusTotal API to ensure safe web interactions. This multi-faceted approach ensures comprehensive security against ransomware threats.

## Key Features
**Real-Time Scanning**: Monitors file system changes in real time using Python Watchdog, providing immediate detection and response to potential ransomware threat.

   ![image](https://github.com/user-attachments/assets/beaca05d-55ec-4b43-a541-33ed818a60c5)
   
   **Deep File Analysis**: Performs in-depth scans by checking file hash values against known malicious hashes, offering a thorough examination of files for hidden threats.
   
   ![image](https://github.com/user-attachments/assets/9de522bc-1e1a-4581-81ad-2b1aed674bae)
   
 Custom Scanning: Utilizes Yara rules to perform tailored scans for detecting specific patterns and behaviors associated with ransomware, allowing for customized threat detection. 
 
   ![image](https://github.com/user-attachments/assets/107a8de3-8ffa-4d7a-8283-3c74889a75c8)
   
 **URL Scanning**: Integrates with the VirusTotal API to analyze URLs for potential security risks, ensuring that web-based content is free from ransomware and other malicious threats.

   ![image](https://github.com/user-attachments/assets/4d04fd64-0cf4-4e15-bb00-c7acfd316418)

 **Flask-Based Interface**: Hosted on a Flask server, providing a user-friendly web interface for managing scans and viewing results, with easy access through a web browser.
 
## Installation

1. **Install Python**: Ensure you have Python 3.6 or higher installed on your system.

2. **Install Required Packages**: Install the necessary Python packages using pip. You can do this with the following command in your Terminal:

    ```bash
    pip install flask colorama watchdog
    ```
3. **Disable Anti-Virus**: Temporarily disable any anti-virus services to ensure uninterrupted scanning.

## Usage

## License

## Contact 


