from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

event_types = ['login_failure', 'file_modified', 'unauthorized_access']

while True:
    event = {
        "timestamp": time.time(),
        "type": random.choice(event_types),
        "details": "Evento gerado para teste"
    }
    producer.send('security-events', event)
    print(f"Evento enviado: {event}")
    time.sleep(2)
