# modules/DataGenerator.py
import random
import hashlib
import datetime
import json
import os


def generate_hash(*args):
    hash_input = ''.join(args).encode()
    return hashlib.sha256(hash_input).hexdigest()


class DataGenerator:
    def __init__(self, storage_path):
        self.storage_path = storage_path
        if not os.path.exists(self.storage_path):
            os.makedirs(self.storage_path)
        self.device_types = ["Satélite", "Nave", "Traje", "Vehículo espacial"]

    def generate_data_log(self, mission_code, cycle_id):
        timestamp = datetime.datetime.now().strftime("%d%m%y%H%M%S")
        status_choices = ['excellent', 'good', 'warning', 'faulty', 'killed', 'unknown']

        num_files = random.randint(1, 100)

        for i in range(num_files):
            device_type = random.choice(self.device_types)  # Randomly select a device type
            device_status = random.choice(status_choices)
            data = {
                'date': timestamp,
                'mission': mission_code,
                'device_type': device_type,  # Assign the random device type
                'device_status': device_status,
                'hash': generate_hash(timestamp, mission_code, device_type, device_status)
            }
            filename = f'APL{mission_code}-{cycle_id:04d}{i:03d}.log'
            self.save_data(filename, data)

    def save_data(self, filename, data):
        filepath = os.path.join(self.storage_path, filename)
        with open(filepath, 'w') as file:
            json.dump(data, file)
