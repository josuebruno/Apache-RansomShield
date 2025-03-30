# scripts/train_model.py

import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# 1. Carregar o CSV
df = pd.read_csv('scripts/training_data.csv')

# 2. Pré-processar
# Transformar 'type' em one-hot encoding
encoder = OneHotEncoder(sparse_output=False)
type_encoded = encoder.fit_transform(df[['type']])
type_labels = encoder.get_feature_names_out(['type'])

# Criar DataFrame com as features
X = pd.DataFrame(type_encoded, columns=type_labels)
y = df['threat']

# 3. Dividir treino/teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Definir o modelo
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(16, activation='relu', input_shape=(X.shape[1],)),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')  # saída binária
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 5. Treinar
model.fit(X_train, y_train, epochs=10, batch_size=16, verbose=1)

# 6. Avaliar
y_pred = (model.predict(X_test) > 0.5).astype("int32")
print(classification_report(y_test, y_pred))

# 7. Salvar o modelo
model.save('scripts/ransomshield_model.h5')
print("✅ Modelo salvo em scripts/ransomshield_model.h5")
