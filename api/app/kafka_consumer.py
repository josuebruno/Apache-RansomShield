from kafka import KafkaConsumer
import json

def consume_kafka_events():
    consumer = KafkaConsumer(
        'security-events',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        group_id='ransomshield-group',
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

    print("Consumidor Kafka iniciado e aguardando eventos...\n")
    for message in consumer:
        event = message.value
        print(f"Evento recebido pelo consumer: {event}")

# Adicione estas linhas abaixo para rodar automaticamente ao executar o script
if __name__ == "__main__":
    consume_kafka_events()
