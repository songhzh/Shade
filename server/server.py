from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

import json
app = Flask(__name__, static_folder="dist", static_url_path="")
CORS(app)

# GET/POST ROUTE
@app.route('/', methods=['GET', 'POST'])
def parse_request():
    return render_template('index.html')
        
        
if __name__ == '__main__':
    app.run(debug=True, port=5000)