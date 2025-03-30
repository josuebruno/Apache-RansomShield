# 🛡️ Apache RansomShield

**Apache RansomShield** é uma plataforma open-source para **prevenção, detecção em tempo real** e **resposta automática** a ataques ransomware em ambientes corporativos.

Utiliza **Apache Kafka** para processar eventos de segurança em tempo real. Em versões futuras, incluirá análise inteligente com **Apache Spark (Machine Learning)** e um **dashboard web em React** para monitoramento centralizado.

---

## 📁 Estrutura do Projeto

apache-ransomshield/
├── api/
│   ├── app/
│   │   ├── main.py
│   │   └── kafka_consumer.py
│   ├── ml/
│   │   └── detection.py
│   ├── config/
│   │   └── settings.py
│   ├── requirements.txt
│   └── Dockerfile
├── kafka/
│   └── docker-compose.yml
├── scripts/
│   └── kafka_producer_test.py
├── web-frontend/             # (em breve)
├── LICENSE
└── README.md

---

## ⚙️ Requisitos

- Docker e Docker Compose  
- Python 3.8+  
- pip e virtualenv  

---

## 🛠️ Instalação e Execução

### 1. Clone o projeto

git clone https://github.com/seu-usuario/apache-ransomshield.git  
cd apache-ransomshield

---

### 2. Inicie Kafka + Zookeeper com Docker

cd kafka  
docker-compose up -d

Isso cria 2 containers:  
Kafka (porta 9092)  
Zookeeper (porta 2181)

---

### 3. Configure o ambiente virtual da API

cd api  
python3 -m venv venv  
source venv/bin/activate  
pip install -r requirements.txt

---

### 4. Inicie o Consumer Kafka (API Flask)

Em um terminal separado:

cd api  
source venv/bin/activate  
python app/kafka_consumer.py

Você verá:

Consumidor Kafka iniciado e aguardando eventos...

---

### 5. Gere eventos com o Kafka Producer (simulação)

Em outro terminal:

pip install kafka-python  
python scripts/kafka_producer_test.py

Saída esperada:

Evento enviado: {'timestamp': ..., 'type': 'unauthorized_access', 'details': 'Evento gerado para teste'}

---

## ✅ Resultado Esperado

Terminal do Producer: envia eventos simulados.  
Terminal do Consumer: consome e imprime os eventos em tempo real.

Exemplo:

Evento recebido pelo consumer: {'timestamp': ..., 'type': 'login_failure', 'details': 'Evento gerado para teste'}

---

## 💡 Exemplo de código: Producer (scripts/kafka_producer_test.py)

from kafka import KafkaProducer  
import json, time, random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

event_types = ['login_failure', 'unauthorized_access', 'file_modified']

while True:
    event = {
        "timestamp": time.time(),
        "type": random.choice(event_types),
        "details": "Evento gerado para teste"
    }
    producer.send('security-events', event)
    print(f"Evento enviado: {event}")
    time.sleep(2)

---

## 💡 Exemplo de código: Consumer (api/app/kafka_consumer.py)

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

if __name__ == "__main__":
    consume_kafka_events()

---

## 🧭 Roadmap do Projeto

Recurso | Status  
--------|--------  
Kafka integrado à API Flask | ✅ Pronto  
Producer para testes | ✅ Pronto  
Análise com Apache Spark | 🔄 Em desenvolvimento  
Dashboard React | 🖥️ Em breve  
Automação de resposta | 🚨 Em breve  

---

## 🤝 Como Contribuir

1. Faça um fork  
2. Crie uma branch: `git checkout -b feature/nova-funcionalidade`  
3. Commit: `git commit -m 'feat: nova funcionalidade'`  
4. Push: `git push origin feature/nova-funcionalidade`  
5. Abra um Pull Request

---

## 📜 Licença

Distribuído sob a licença Apache 2.0.

---

Desenvolvido com ❤️ por [Seu Nome ou Equipe]
