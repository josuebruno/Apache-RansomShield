import sys
import os
import json

# Adiciona o diretório raiz ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS  # Habilita CORS
from ml.detection import analyze_logs

app = Flask(__name__)
CORS(app)  # Libera acesso CORS para todos os domínios
api = Api(app)

# Caminho para o arquivo de eventos
EVENT_LOG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../scripts/event_log.json'))

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({"status": "Apache RansomShield Online!"})

@app.route('/api/analyze', methods=['POST'])
def analyze():
    result = analyze_logs()
    return jsonify(result)

@app.route('/api/events', methods=['GET'])
def get_events():
    if os.path.exists(EVENT_LOG_PATH):
        with open(EVENT_LOG_PATH, "r") as f:
            lines = f.readlines()[-50:]  # mostra os últimos 50 eventos
            events = [json.loads(line) for line in lines]
        return jsonify(events)
    else:
        return jsonify([])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
