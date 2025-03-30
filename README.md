# 🛡️ Apache RansomShield

**Apache RansomShield** é uma plataforma open-source para **prevenção, detecção em tempo real** e **resposta automática** a ataques ransomware em ambientes corporativos.

Utiliza **Apache Kafka** para processar eventos de segurança em tempo real.  
Possui integração com **Apache Spark**, **Flask API**, um modelo de **IA com TensorFlow** e um **dashboard React** para monitoramento visual de eventos classificados como ameaça.

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
│   ├── train_model.py
│   └── event_log.json
├── models/
│   └── ransomshield_model.h5
├── web-frontend/
│   ├── index.html
│   ├── package.json
│   ├── src/
│   │   └── App.jsx
├── LICENSE
└── README.md
```

---

## ⚙️ Requisitos

- Docker e Docker Compose
- Python 3.8+
- pip e virtualenv
- Java 8 ou 11
- Node.js (para o dashboard React)

---

## 🛠️ Instalação e Execução

### 1. Clone o projeto

```bash
git clone https://github.com/josuebruno/apache-ransomshield.git
cd apache-ransomshield
```

### 2. Suba Kafka + Zookeeper com Docker

```bash
cd kafka
docker-compose up -d
```

---

### 3. Configure a API Python

```bash
cd api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 4. Inicie o consumidor Kafka com IA

```bash
cd api
source venv/bin/activate
python app/kafka_consumer.py
```

---

### 5. Execute o producer para gerar eventos simulados

```bash
python scripts/kafka_producer_test.py
```

---

### 6. Processamento com Apache Spark (stream)

```bash
spark-submit \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1 \
  spark_stream.py
```

---

### 7. Geração de dados para treino (IA)

```bash
python scripts/generate_training_data.py
```

---

### 8. Treinar modelo de IA com TensorFlow

```bash
python scripts/train_model.py
```

> Modelo será salvo em `scripts/ransomshield_model.h5`

---

### 9. Iniciar a API Flask (para o dashboard)

```bash
cd api
source venv/bin/activate
python app/main.py
```

---

### 10. Iniciar o dashboard React

```bash
cd web-frontend
npm install
npm run dev
```

Acesse o painel em: [http://localhost:5173](http://localhost:5173)

---

## ✅ Resultado Esperado

- Producer envia eventos simulados.
- Kafka Consumer classifica os eventos com IA.
- Logs salvos no arquivo `scripts/event_log.json`.
- Dashboard React exibe eventos em tempo real.

---

## 💡 Exemplo de Evento

```json
{
  "timestamp": 1743368209.8566306,
  "type": "unauthorized_access",
  "details": "Evento gerado para teste",
  "status": "threat"
}
```

---

## 🧠 IA com TensorFlow

- Rede neural MLP simples
- Classificação binária (0 = normal, 1 = ameaça)
- Treinada com tipos: `login_failure`, `unauthorized_access`, `file_modified`
- Pode ser re-treinada com novos eventos

---

## 🖥️ Dashboard React

- Leitura periódica do endpoint Flask `/api/events`
- Interface com destaque de ameaças
- Exibição em tempo real dos logs do Kafka

---

## 🧭 Roadmap do Projeto

| Recurso                      | Status        |
|------------------------------|---------------|
| Kafka integrado à API Flask | ✅ Pronto
| Producer para testes         | ✅ Pronto
| Análise com Apache Spark     | ✅ Em uso
| IA com TensorFlow            | ✅ Treinada
| Dashboard React              | ✅ Em uso
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
