# api/app/kafka_consumer.py

from kafka import KafkaConsumer
import json
import tensorflow as tf
import numpy as np
from sklearn.preprocessing import OneHotEncoder
import os

# Carregar o modelo treinado (caminho relativo ao script)
model = tf.keras.models.load_model('../../scripts/ransomshield_model.h5')

# Criar o codificador de tipo (deve bater com os usados no treino)
encoder = OneHotEncoder(sparse_output=False)
encoder.fit([["login_failure"], ["unauthorized_access"], ["file_modified"]])

# Caminho absoluto do arquivo de log
log_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../scripts/event_log.json'))

# Garante que o diretório exista
os.makedirs(os.path.dirname(log_path), exist_ok=True)

# Cria o arquivo se ainda não existir
if not os.path.exists(log_path):
    open(log_path, 'w').close()

def classificar_evento(event_type):
    encoded = encoder.transform([[event_type]])
    prediction = model.predict(encoded)[0][0]
    return 1 if prediction >= 0.5 else 0

def consume_kafka_events():
    consumer = KafkaConsumer(
        'security-events',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        group_id='ransomshield-group',
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

    print("🛡️ Consumidor Kafka com IA iniciado...\n")

    for message in consumer:
        event = message.value
        threat = classificar_evento(event['type'])

        status = "🚨 AMEAÇA DETECTADA" if threat else "✅ Evento normal"
        print(f"\n📦 Evento: {event}")
        print(f"🤖 Classificação IA: {status}")

        # Salvar evento para o dashboard
        with open(log_path, 'a') as f:
            f.write(json.dumps({
                "timestamp": event['timestamp'],
                "type": event['type'],
                "details": event['details'],
                "status": "threat" if threat else "normal"
            }) + "\n")

if __name__ == "__main__":
    consume_kafka_events()
