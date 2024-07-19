import requests
import sys

def scan_url_for_malware(url, api_key, output_file):
    try:
        # Construct the API endpoint
        endpoint = f'https://www.virustotal.com/vtapi/v2/url/scan'
        
        # Set the parameters
        params = {'apikey': api_key, 'url': url}
        
        # Make the request to submit the URL for scanning
        response = requests.post(endpoint, data=params)
        
        # Check if the request was successful
        if response.status_code == 200:
            json_response = response.json()
            if json_response['response_code'] == 1:
                print("URL submitted successfully for scanning.")
                # Get the scan ID for retrieving the report
                scan_id = json_response['scan_id']
                # Now, we can retrieve the report for this scan ID
                retrieve_url_scan_report(scan_id, api_key, output_file)
            else:
                print("Error:", json_response['verbose_msg'])
        else:
            print("Failed to submit URL for scanning. Status code:", response.status_code)
            print("Response:", response.text)
    except Exception as e:
        print("An error occurred while scanning the URL:", e)

def retrieve_url_scan_report(scan_id, api_key, output_file):
    try:
        # Construct the API endpoint
        endpoint = f'https://www.virustotal.com/vtapi/v2/url/report'
        
        # Set the parameters
        params = {'apikey': api_key, 'resource': scan_id}
        
        # Make the request to retrieve the scan report
        response = requests.get(endpoint, params=params)
        
        # Check if the request was successful
        if response.status_code == 200:
            json_response = response.json()
            if json_response['response_code'] == 1:
                print("Scan report retrieved successfully.")
                # Write the report to the output file
                with open(output_file, 'w') as f:
                    for scan_result in json_response['scans'].items():
                        file_name = scan_result[0]
                        detected = scan_result[1]['detected']
                        result = scan_result[1]['result']
                        f.write(f"{file_name},{detected},{result}\n")
                print("Scan report saved to:", output_file)
            else:
                print("Error:", json_response['verbose_msg'])
        else:
            print("Failed to retrieve scan report. Status code:", response.status_code)
            print("Response:", response.text)
    except Exception as e:
        print("An error occurred while retrieving the scan report:", e)

# Prompt the user to input the URL
#url_to_scan = input("Enter the URL you want to scan for malware: ")
url_to_scan = sys.argv[1]

# Prompt the user to input their VirusTotal API key
api_key = "f664191271d0081fbb9d321039d2f5335412a267f13597814d0025f366d0bc6b"

# Define the output file name
output_file = "templates/scan_report.csv"

# Scan the URL for malware and save the report to the output file
scan_url_for_malware(url_to_scan, api_key, output_file)