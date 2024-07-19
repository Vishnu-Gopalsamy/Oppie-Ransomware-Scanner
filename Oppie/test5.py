import os
import subprocess
import itertools
import time
import sys
from colorama import Fore

def count_and_collect_yara_files(yara_dir):
    yara_files = []
    num_yara_files = 0
    num_yar_files = 0
    
    # Traverse the directory recursively
    for root, dirs, files in os.walk(yara_dir):
        for file in files:
            if file.endswith('.yara') or file.endswith('.yar'):
                yara_files.append(os.path.join(root, file))
                if file.endswith('.yara'):
                    num_yara_files += 1
                elif file.endswith('.yar'):
                    num_yar_files += 1
    
    print(f"Number of .yara files found: {num_yara_files}")
    print(f"Number of .yar files found: {num_yar_files}")
    
    return yara_files

def run_yara_on_directory_batch(yara_files_batch, target_dir, output_file):
    # Build the command to execute YARA rules on the target directory
    command = ['yara64'] + yara_files_batch + [target_dir]
    
    # Execute the YARA command using subprocess
    try:
        #print(Fore.RED)
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        #print(Fore.WHITE)
        
        # Get the YARA scan output
        yara_output = result.stdout
        
        # Append the YARA output to the output file
        with open(output_file, 'a') as f:
            f.write(yara_output)
            f.write('\n\n')  # Add separator between batch outputs
            
        #print(Fore.GREEN)
        #print("YARA scan batch completed successfully.")
        #print(Fore.WHITE)
        
    except subprocess.CalledProcessError as e:
        #print(Fore.YELLOW)
        #print(f"YARA execution failed with error: {e}")
        #print(Fore.WHITE)
        pass

def run_yara_on_directory(yara_files, target_dir, output_file, batch_size=50):
    # Create the output file (or clear its contents if it already exists)
    with open(output_file, 'w') as f:
        f.write("")  # Clear the file contents or create an empty file
    
    # Calculate total number of batches based on batch size
    total_batches = (len(yara_files) + batch_size - 1) // batch_size
    
    # Split the list of YARA rule files into batches
    for i in range(0, len(yara_files), batch_size):
        yara_files_batch = yara_files[i:i+batch_size]
        
        # Loading animation characters
        #animation = itertools.cycle(['|', '/', '-', '\\'])
        
        # Print a loading animation while processing the batch
        #for _ in range(total_batches):  # Use total_batches for animation cycles
            #time.sleep(0.2)  # Adjust the animation speed (seconds)
            #print(f"\rProcessing batch {i//batch_size + 1}/{total_batches}... {next(animation)}", end='', flush=True)
        
        # Call function to run YARA on the batch
        run_yara_on_directory_batch(yara_files_batch, target_dir, output_file)
        #print("")  # Move to a new line after batch completion

if __name__ == "__main__":
    # Get the current directory of the script
    current_dir = os.path.dirname(__file__)
    
    # Specify the directory containing your YARA rules
    yara_directory = os.path.join(current_dir, 'rule_dir')
    
    # Specify the target directory to scan with YARA
    #target_directory = os.path.join(current_dir, 'The-MALWARE-Repo-master', 'Ransomware')
    #target_directory = os.path.join(current_dir, 'sample')
    target_directory = sys.argv[1]
    # Specify the output file to save all YARA scan results
    output_file = os.path.join(current_dir, 'yara_scan_results.txt')
    
    # Count and collect all YARA rule files recursively
    yara_files = count_and_collect_yara_files(yara_directory)
    
    # Specify the batch size for processing YARA rule files
    batch_size = 50
    
    # Call the function to run YARA on the target directory using collected rules in batches
    run_yara_on_directory(yara_files, target_directory, output_file, batch_size)
    
    print("Scan Successfully Completed " + target_directory)
    
    
    
exec(open('ana4.py').read())
