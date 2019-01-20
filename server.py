from flask import Flask, request, jsonify, render_template, send_file
from flask_cors import CORS
import json
import os
from encryption import Encryption
app = Flask(__name__, static_folder="dist", static_url_path="")
CORS(app)
UPLOAD_FOLDER = os.path.basename('/images')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def decode_file():
    bb = Encryption.decode('images/key.png', 'images/enc.png')
    with open("decoded.txt", 'w') as fout:
        for byte in bb.bytes:
            fout.write(str(chr(byte)))
# GET/POST ROUTE
@app.route('/', methods=['GET', 'POST'])
def parse_request():
    return render_template('index.html')
        
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    
    file.save(f)

    decode_file()
    
    filename = 'decoded.txt'
    
    return send_file(filename , attachment_filename=filename, as_attachment=True)

     
if __name__ == '__main__':
    app.run(debug=True, port=5000)