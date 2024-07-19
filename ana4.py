import os
import csv

# Function to analyze the scanner file and generate a report
def analyze_scanner_file(scanner_file):
    report = {}

    # Open the scanner file
    with open(scanner_file, 'r') as file:
        for line in file:
            # Skip empty lines
            if not line.strip():
                continue
            
            # Split each line into malware type and file path
            parts = line.strip().split(' ', 1)
            if len(parts) != 2:
                print(f"Ignoring line: {line.strip()}")
                continue
            
            malware_type, file_path = parts
            # Extract the filename
            filename = os.path.basename(file_path)

            # Check if the filename is already in the report, if not, initialize it
            if filename not in report:
                report[filename] = []

            # Append the malware type to the filename entry
            report[filename].append(malware_type)

    return report

# Function to generate and save the report as a CSV file
def generate_csv_report(report, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['File', 'Malware Types']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for filename, malware_types in report.items():
            writer.writerow({'File': filename, 'Malware Types': ', '.join(malware_types)})

# Main function
def main():
    scanner_file = "yara_scan_results.txt"  # Replace with the path to your scanner file
    output_file = "templates/malware_report.csv"  # Output CSV file path
    report = analyze_scanner_file(scanner_file)
    generate_csv_report(report, output_file)
    #print(f"Report generated and saved as '{output_file}'.")

if __name__ == "__main__":
    main()
