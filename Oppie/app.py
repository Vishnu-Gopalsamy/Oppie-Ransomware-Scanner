import os
from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__, static_url_path='/static')

# Define the index route
@app.route('/image')
def get_image():
    # Path to the directory containing the image
    image_directory = os.path.join(app.root_path, 'static')
    # Name of the image file
    image_filename = 'op.png'
    # Return the image file to the client
    return send_from_directory(image_directory, image_filename)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/yara')
def yara():
    return render_template('yara.html')

@app.route('/mal')
def mal():
    return render_template('hashes.csv')

@app.route('/urlindex')
def urlpage():
    return render_template('url.html')

@app.route('/urlr')
def urlresult():
    return render_template('scan_report.csv')

@app.route('/deepScanResult')
def deepscanresult():
    return render_template('Deepresults.csv')

@app.route('/deepScan')
def deepScanPage():
    return render_template('DeepScan.html')

@app.route('/yaraReport')
def yaraReport():
    return render_template('malware_report.csv')







# Define the route to process the input text (path)
@app.route('/process', methods=['POST'])
def process_path():
    try:
        # Get the input path from the JSON request data
        input_path = request.get_json()
        #input_path = data['inputPath']
      
        inputTextValue = input_path['inputText']
        
        print(inputTextValue)

        # Execute scanner.py with the input path as command-line argument
        result = subprocess.run(['python', 'PythonAutomatedYara.py', inputTextValue], capture_output=True, text=True)
        print(result)
        if result.returncode == 0:
            # Process the scanner output
            scan_result = result.stdout.strip()
            return jsonify({'result': scan_result})
        else:
            return jsonify({'error': 'Scanner execution failed'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 600
    
@app.route('/urlscan', methods=['POST'])
def urlscan():
    try:
        # Get the input path from the JSON request data
        input_path = request.get_json()
        inputurl = input_path['inputText']
     
        
        
        print(inputurl)
        
        # Execute scanner.py with the input path as command-line argument
        result = subprocess.run(['python', 'url.py', inputurl], capture_output=True, text=True)
        print(result)
        if result.returncode == 0:
            # Process the scanner output
            scan_result = result.stdout.strip()
            return jsonify({'result': scan_result})
        else:
            return jsonify({'error': 'Scanner execution failed'}), 500

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 650
    
@app.route('/deepscan', methods=['POST'])
def deepscan():
    try:
        # Get the input path from the JSON request data
        input_path = request.get_json()
        inputurl = input_path['inputText']
     
        
        
        print(inputurl)
        
        # Execute scanner.py with the input path as command-line argument
        result = subprocess.run(['python', 'DeepScan.py', inputurl], capture_output=True, text=True)
        print(result)
        if result.returncode == 0:
            # Process the scanner output
            scan_result = result.stdout.strip()
            return jsonify({'result': scan_result})
        else:
            return jsonify({'error': 'Scanner execution failed'}), 500

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 650

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
