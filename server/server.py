from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json
import os

app = Flask(__name__, static_folder="dist", static_url_path="")
CORS(app)
UPLOAD_FOLDER = os.path.basename('../images')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# GET/POST ROUTE
@app.route('/', methods=['GET', 'POST'])
def parse_request():
    return render_template('index.html')
        
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    
    file.save(f)

    return render_template('index.html')
        
if __name__ == '__main__':
    app.run(debug=True, port=5000)