# Apolo11Simulation.py
from random import choice
import threading
import time
import os
import glob


class Apolo11Simulation:
    def __init__(self, data_generator, file_manager, report_generator):
        self.data_generator = data_generator
        self.file_manager = file_manager
        self.report_generator = report_generator
        self.running = False

    def start_simulation(self, interval=20):
        self.running = True
        cycle_id = 0
        while self.running:
            cycle_id += 1
            mission_code = choice(["ORBONE", "CLNM", "TMRS", "GALXONE", "UNKN"])
            self.data_generator.generate_data_log(mission_code, cycle_id)
            self.report_generator.generate_reports(cycle_id)
            self.move_processed_files_to_backup()
            time.sleep(interval)

    def stop_simulation(self):
        self.running = False

    def move_processed_files_to_backup(self):
        files_to_move = glob.glob(os.path.join(self.data_generator.storage_path, '*.log'))
        for file_path in files_to_move:
            filename = os.path.basename(file_path)
            self.file_manager.move_to_backup(filename)

    def run(self):
        simulation_thread = threading.Thread(target=self.start_simulation)
        simulation_thread.start()
