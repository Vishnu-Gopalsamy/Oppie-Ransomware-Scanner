import sys
import os
import time
def scan_file(file_path):
    try:
        if os.path.isfile(file_path):
            # Perform a basic scan operation (example: count lines in the file)
            with open(file_path, 'r') as file:
                line_count = sum(1 for line in file)
                time.sleep(5.0)
                return f"File scanned successfully. Line count: {line_count}"
        elif os.path.isdir(file_path):
            return "Scanning directory is not supported in this example."
        else:
            return "Invalid file or directory path."
    except Exception as e:
        return f"Error occurred during scanning: {str(e)}"

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python scanner.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    scan_result = scan_file(file_path)
    print(scan_result)
