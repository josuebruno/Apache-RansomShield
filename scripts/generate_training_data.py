# scripts/generate_training_data.py

import csv
import random
import time

event_types = ['login_failure', 'unauthorized_access', 'file_modified']

# Simulando 1000 eventos com labels
with open('scripts/training_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['timestamp', 'type', 'threat'])  # Cabeçalho

    for _ in range(1000):
        t = random.choice(event_types)
        ts = time.time()

        # Lógica simples de "ameaça" só pra treinar
        threat = 1 if t in ['unauthorized_access', 'file_modified'] else 0

        writer.writerow([ts, t, threat])
        time.sleep(0.001)  # opcional
