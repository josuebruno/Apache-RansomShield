from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, DoubleType

# Define o esquema do JSON vindo do Kafka
schema = StructType() \
    .add("timestamp", DoubleType()) \
    .add("type", StringType()) \
    .add("details", StringType())

# Cria sessão Spark
spark = SparkSession.builder \
    .appName("RansomShieldSparkStream") \
    .getOrCreate()

# Lê o stream do Kafka
df_raw = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "security-events") \
    .load()

# Converte os dados do Kafka (value é binário) em JSON
df_parsed = df_raw.selectExpr("CAST(value AS STRING) as json") \
    .select(from_json(col("json"), schema).alias("data")) \
    .select("data.*")

# Apenas para exibir os eventos filtrados
df_filtered = df_parsed.filter(col("type") == "unauthorized_access")

# Exibe no console
query = df_filtered.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
