import hashlib
import pandas as pd
import os
import csv
import time

def generate_hash(file_path, hash_type='md5'):
    if hash_type == 'md5':
        hash_obj = hashlib.md5()
    elif hash_type == 'sha1':
        hash_obj = hashlib.sha1()
    elif hash_type == 'sha256':
        hash_obj = hashlib.sha256()
    else:
        raise ValueError("Invalid hash type")

    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

def main():
    while True:
        file_path = "templates/buffer_filepath.csv"
        if os.path.getsize(file_path) == 0:
            #print("buffer_filepath.csv is empty, skipping this iteration...")
            time.sleep(3)
            continue

        df = pd.read_csv(file_path, header=None)
        if df.empty:
            #print("buffer_filepath.csv is empty, skipping this iteration...")
            continue

        hashes = []
        #print("hashes found")
        for file_path in df[0]:
            file_path = file_path.strip()
            if os.path.isfile(file_path):
                md5 = generate_hash(file_path, 'md5')
                sha1 = generate_hash(file_path, 'sha1')
                sha256 = generate_hash(file_path, 'sha256')
                hashes.append([file_path, md5, sha1, sha256])
            else:
                print(f"File not found: {file_path}")

        with open("templates/hashes.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["file_path", "md5", "sha1", "sha256"])
            writer.writerows(hashes)

        with open("templates/MalHash.csv", "r") as f:
            reader = csv.reader(f)
            hashes_to_match = [row[0] for row in reader]

        with open("templates/hashes.csv", "r") as f:
            reader = csv.reader(f)
            warning = open("Warning.txt","a")
            next(reader)  # Skip header row
            for row in reader:
                file_path, md5, sha1, sha256 = row
                if md5 in hashes_to_match or sha1 in hashes_to_match or sha256 in hashes_to_match:
                    print(f"Warning::Suspicious File:::path: {file_path}")
                    warning.write(f"Warning::Suspicious File:::path: {file_path} \n")
                    #need to add a file wirter here
                    

        # Truncate the buffer_filepath.csv file
        with open("templates/buffer_filepath.csv", "w", newline='') as f:
            pass

        # Wait for 3 seconds before reading the buffer_filepath.csv file again
        time.sleep(3)

if __name__ == "__main__":
    main()