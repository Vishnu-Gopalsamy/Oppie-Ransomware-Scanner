import os
import csv
import hashlib
import sys

def generate_hashes(directory, output_csv):
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for root, dirs, files in os.walk(directory):
            for file in files:
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'rb') as f:
                        file_hash = hashlib.sha256()
                        while chunk := f.read(4096):
                            file_hash.update(chunk)
                        writer.writerow([filepath, file, file_hash.hexdigest()])
                except Exception as e:
                    pass
                    #print(f"Error hashing {filepath}: {e}")

def scan_for_ransomware(analysis_csv, malware_csv, results_csv):
    detected = []
    with open(analysis_csv, 'r') as analysis_file:
        analysis_reader = csv.reader(analysis_file)
        analysis_data = {(row[0], row[1]): row[2] for row in analysis_reader}

    with open(malware_csv, 'r') as malware_file:
        malware_reader = csv.reader(malware_file)
        malware_hashes = {row[0] for row in malware_reader}

    for (filepath, filename), hash_val in analysis_data.items():
        if hash_val in malware_hashes:
            detected.append((filepath, filename))

    with open(results_csv, 'w', newline='') as results_file:
        writer = csv.writer(results_file)
        writer.writerow(["File Name", "File Path"])
        for file_path, file_name in detected:
        
            writer.writerow([file_name, file_path])

    return detected

if __name__ == '__main__':

    directory_to_scan = sys.argv[1]
    analysis_csv = 'analysis.csv'
    malware_csv = "templates/Malhash.csv"
    results_csv = 'templates/Deepresults.csv'

    # Generate hashes for files in directory and store in analysis.csv
    generate_hashes(directory_to_scan, analysis_csv)

    # Scan for ransomware
    detected_files = scan_for_ransomware(analysis_csv, malware_csv, results_csv)

    if detected_files:
        print("Ransomware detected! Results saved in", results_csv)
    else:
        print("No ransomware detected.")

    # Delete the analysis.csv file
    try:
        os.remove(analysis_csv)
    except Exception as e:
        print(f"Error deleting analysis file: {e}")
