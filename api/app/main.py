from flask import Flask, jsonify
from flask_restful import Api
from ml.detection import analyze_logs

app = Flask(__name__)
api = Api(app)

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({"status": "Apache RansomShield Online!"})

@app.route('/api/analyze', methods=['POST'])
def analyze():
    result = analyze_logs()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
