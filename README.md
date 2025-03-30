# 🛡️ Apache RansomShield

**Apache RansomShield** é uma plataforma open-source para **prevenção, detecção em tempo real** e **resposta automática** a ataques ransomware em ambientes corporativos.

Utiliza **Apache Kafka** para processar eventos de segurança em tempo real.  
Já possui integração com **Apache Spark**, **Flask API**, e um **modelo de IA com TensorFlow** para detecção de ameaças.

---

## 📁 Estrutura do Projeto

```
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
│   ├── kafka_producer_test.py
│   ├── generate_training_data.py
│   └── train_model.py
├── models/
│   └── ransomshield_model.h5
├── web-frontend/             # (em breve)
├── LICENSE
└── README.md
```

---

## ⚙️ Requisitos

- Docker e Docker Compose  
- Python 3.8+  
- pip e virtualenv  
- Java 8 ou 11 (recomendado)  
  - Verifique com: `java -version`  
  - Defina JAVA_HOME se necessário:
    ```bash
    export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
    ```

---

## 🛠️ Instalação e Execução

### 1. Clone o projeto

```bash
git clone https://github.com/josuebruno/apache-ransomshield.git
cd apache-ransomshield
```

### 2. Inicie Kafka + Zookeeper com Docker

```bash
cd kafka
docker-compose up -d
```

### 3. Configure o ambiente virtual da API

```bash
cd api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Inicie o Consumer Kafka (API Flask)

```bash
cd api
source venv/bin/activate
python app/kafka_consumer.py
```

### 5. Gere eventos com o Kafka Producer

```bash
python scripts/kafka_producer_test.py
```

### 6. Inicie a análise com Apache Spark

```bash
spark-submit \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1 \
  spark_stream.py
```

> Esse comando executa o Spark com o conector Kafka necessário para streaming.  
> Certifique-se de que o Kafka esteja rodando e o Java instalado/configurado.

---

### 7. Gerar dados de treino para IA

```bash
python scripts/generate_training_data.py
```

---

### 8. Treinar modelo de IA (MLP com TensorFlow)

```bash
python scripts/train_model.py
```

> O modelo será salvo em: `scripts/ransomshield_model.h5`

---

## ✅ Resultado Esperado

- Terminal do **Producer**: envia eventos simulados
- Terminal do **Consumer ou Spark**: exibe os eventos
- IA treinada salva e pronta para uso

---

## 💡 Exemplo de evento gerado

```json
{
  "timestamp": 1743363001.63,
  "type": "unauthorized_access",
  "details": "Evento gerado para teste"
}
```

---

## 🧠 Sobre o Modelo de IA

O modelo atual é um **MLP simples (rede neural)** que classifica os eventos em `ameaça (1)` ou `normal (0)` com base no tipo de evento.

- Treinado com `TensorFlow` e `scikit-learn`
- Usa `one-hot encoding` dos tipos de evento
- Pode ser facilmente re-treinado com eventos mais ricos no futuro

---

## 📦 Escalabilidade futura

- ✅ IA já integrada e adaptável
- 🔄 Em breve: dashboard em React
- 🚨 Automação de resposta com agentes distribuídos
- 📡 Suporte para coleta remota de eventos (via REST ou socket)
- 📈 Possibilidade de salvar logs em bancos NoSQL (MongoDB, Elastic)

---

## 🧭 Roadmap do Projeto

| Recurso                      | Status        |
|------------------------------|----------------|
| Kafka integrado à API Flask | ✅ Pronto
| Producer para testes         | ✅ Pronto
| Análise com Apache Spark     | ✅ Em uso
| IA com TensorFlow            | ✅ Treinada
| Dashboard React              | 🖥️ Em breve
| Automação de resposta        | 🚨 Em breve

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

Desenvolvido com ❤️ por **Josue Bruno**
