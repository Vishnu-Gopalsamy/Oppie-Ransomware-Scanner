def find_detected_ransomwares(input_file, output_file):
    # Set to store unique ransomware names detected
    detected_ransomwares = set()

    # Open the input file containing YARA search results
    with open(input_file, 'r') as f:
        lines = f.readlines()

        # Process each line in the file
        for line in lines:
            # Strip whitespace characters (including newline)
            line = line.strip()

            if line:
                # Split the line into ransomware name and YARA rule name
                parts = line.split()

                if len(parts) >= 2:
                    ransomware_name = parts[1]  # Ransomware name is assumed to be the second part
                    detected_ransomwares.add(ransomware_name)

    # Open a new text file to write the detected ransomware names
    with open(output_file, 'w') as f:
        f.write("Detected Ransomwares:\n")
        for ransomware_name in detected_ransomwares:
            f.write(f"{ransomware_name}\n")

if __name__ == "__main__":
    # Path to the input file containing YARA search results
    input_file_path = "yara_scan_results.txt"

    # Path to the output file to write the detected ransomware names
    output_file_path = "analysis.txt"

    # Find and write the detected ransomware names to the output file
    find_detected_ransomwares(input_file_path, output_file_path)

    #print(f"Detected ransomware names written to {output_file_path}")
    
    
    f = open('analysis.txt','r')
    print(f.read())
    exec(open('ana3_1.py').read())
