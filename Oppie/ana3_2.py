def find_most_repeated_rules(input_file, output_file):
    # Dictionary to store ransomware names and associated YARA rule frequencies
    ransomware_rules_counts = {}

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
                    rule_name = parts[0]  # YARA rule name is assumed to be the first part

                    # Update the count of the rule name for the ransomware in the dictionary
                    if ransomware_name in ransomware_rules_counts:
                        if rule_name in ransomware_rules_counts[ransomware_name]:
                            ransomware_rules_counts[ransomware_name][rule_name] += 1
                        else:
                            ransomware_rules_counts[ransomware_name][rule_name] = 1
                    else:
                        ransomware_rules_counts[ransomware_name] = {rule_name: 1}

    # Open a new text file to write the most repeated rules for each ransomware
    with open(output_file, 'w') as f:
        for ransomware_name, rule_counts in ransomware_rules_counts.items():
            # Write ransomware name and associated rule counts
            f.write(f"Ransomware: {ransomware_name}\n")
            # Sort rule names based on their frequencies in descending order
            sorted_rules = sorted(rule_counts.items(), key=lambda x: (-x[1], x[0]))
           # print(sorted_rules)
            f.write(f"Rule: ")
            for rule_name, count in sorted_rules:
                f.write(f"{rule_name} ")
            f.write("\n")  # Add a blank line to separate ransomware entries

if __name__ == "__main__":
    # Path to the input file containing YARA search results
    input_file_path = "yara_scan_results.txt"

    # Path to the output file to write the most repeated rules for each ransomware
    output_file_path = "analysis_IT.txt"

    # Find and write the most repeated YARA rules for each ransomware to the output file
    find_most_repeated_rules(input_file_path, output_file_path)

    print(f"Most repeated YARA rules for each ransomware written to {output_file_path}")
    
    f = open("analysis_IT.txt")
    
    print(f.read())
    
    f.close()