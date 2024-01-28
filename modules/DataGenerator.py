# modules/DataGenerator.py

import random
import hashlib
import datetime
import json
import os


def generate_hash(*args):
    """
    Genera un hash SHA256 a partir de los argumentos proporcionados.
    """
    hash_input = ''.join(args).encode()
    return hashlib.sha256(hash_input).hexdigest()


class DataGenerator:
    """
    Esta clase representa el generador de datos de la simulación de Apollo 11.
    Se encarga de generar datos de log para la simulación.
    """

    def __init__(self, storage_path):
        """
        Inicializa el generador de datos con la ruta al directorio de almacenamiento.
        Si el directorio de almacenamiento no existe, lo crea.
        """
        self.storage_path = storage_path
        if not os.path.exists(self.storage_path):
            os.makedirs(self.storage_path)
        self.device_types = ["Satélite", "Nave", "Traje", "Vehículo espacial"]

    def generate_data_log(self, mission_code, cycle_id):
        """
        Genera los datos de log para una misión y un ciclo de simulación.
        """
        timestamp = datetime.datetime.now().strftime("%d%m%y%H%M%S")
        status_choices = ['excellent', 'good', 'warning', 'faulty', 'killed', 'unknown']

        num_files = random.randint(1, 100)

        for i in range(num_files):
            device_type = random.choice(self.device_types)  # Selecciona aleatoriamente un tipo de dispositivo
            device_status = random.choice(status_choices)
            data = {
                'date': timestamp,
                'mission': mission_code,
                'device_type': device_type,  # Asigna el tipo de dispositivo aleatorio
                'device_status': device_status,
                'hash': generate_hash(timestamp, mission_code, device_type, device_status)
            }
            filename = f'APL{mission_code}-{cycle_id:04d}{i:03d}.log'
            self.save_data(filename, data)

    def save_data(self, filename, data):
        """
        Guarda los datos generados en un archivo JSON.
        """
        filepath = os.path.join(self.storage_path, filename)
        with open(filepath, 'w') as file:
            json.dump(data, file)
