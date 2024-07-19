import os
import subprocess
import itertools
import time
from colorama import Fore
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import joblib
import sys

# Function to extract features from files
def extract_features_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
    return content

# Function to traverse the specified directory and extract features from files
def extract_features_from_directory(directory):
    files = []
    features = []
    labels = []
    for root, dirs, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            files.append(file_path)
            content = extract_features_from_file(file_path)
            if content.strip():  # Check if content is not empty
                features.append(content)
                # Labeling files as benign (0) or malicious (1) based on directory structure
                if "benign" in root:
                    labels.append(0)
                else:
                    labels.append(1)
    return files, features, labels

# Function to run YARA search
def run_yara_search(yara_dir, target_dir, output_file):
    # Your YARA search code here...
    pass

# Function to integrate YARA search and ransomware detection
def integrate_yara_and_ransomware_detection(yara_dir, target_dir, output_file):
    # Run YARA search to identify potential ransomware files
    run_yara_search(yara_dir, target_dir, output_file)
    
    # Run ransomware detection on identified ransomware files
    directory = target_dir  # Use the same target directory as YARA search
    files, features, labels = extract_features_from_directory(directory)
    
    # Convert features to TF-IDF vectors
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(features)
    
    # Load the trained model and vectorizer
    classifier = joblib.load('ransomware_detector_model.joblib')
    
    # Predict labels using the classifier
    y_pred = classifier.predict(X)
    
    # Write detected ransomware names into a text file
    detected_ransomwares = [os.path.basename(files[i]) for i in range(len(y_pred)) if y_pred[i] == 1]
    if detected_ransomwares:
        with open("detected_ransomwares.txt", "w") as f:
            f.write("Detected Ransomware Names:\n")
            for ransomware_name in detected_ransomwares:
                f.write(ransomware_name + "\n")

# Example usage
if __name__ == "__main__":
    # Specify directories
    current_dir = os.path.dirname(__file__)
    yara_directory = os.path.join(current_dir, 'rule_dir')
    target_directory = sys.argv[1]
    
    # Specify output file for YARA search
    yara_output_file = os.path.join(current_dir, 'yara_scan_results.txt')
    
    # Run YARA search and ransomware detection
    integrate_yara_and_ransomware_detection(yara_directory, target_directory, yara_output_file)
