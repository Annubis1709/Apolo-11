import random
import threading
import time
import os
import glob

from modules.ControlDashboard import ControlDashboard
from modules.DataGenerator import DataGenerator
from modules.FileManager import FileManager
from modules.ReportGenerator import ReportGenerator


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
            mission_code = random.choice(["ORBONE", "CLNM", "TMRS", "GALXONE", "UNKN"])
            self.data_generator.generate_data_log(mission_code, cycle_id)
            self.report_generator.generate_reports()
            self.move_processed_files_to_backup()
            time.sleep(interval)

    def stop_simulation(self):
        self.running = False

    def move_processed_files_to_backup(self):
        # Obtiene todos los archivos .log de la ruta de almacenamiento de datos
        files_to_move = glob.glob(os.path.join(self.data_generator.storage_path, '*.log'))
        for file_path in files_to_move:
            # Extrae el nombre del archivo de la ruta
            filename = os.path.basename(file_path)
            # Mueve el archivo al directorio de respaldo (backup)
            self.file_manager.move_to_backup(filename)

    def run(self):
        simulation_thread = threading.Thread(target=self.start_simulation)
        simulation_thread.start()


# A continuación se muestra un ejemplo de cómo puede inicializar y ejecutar la simulación:

if __name__ == '__main__':
    base_path = os.path.dirname(os.path.abspath(__file__))  # Directorio raíz del proyecto
    components = ['satellite', 'spacesuit', 'vehicle']

    data_generator = DataGenerator(os.path.join(base_path, 'devices'))
    file_manager = FileManager(base_path)
    report_generator = ReportGenerator(os.path.join(base_path, 'reports'))
    control_dashboard = ControlDashboard(report_generator.storage_path)
    simulation = Apolo11Simulation(data_generator, file_manager, report_generator)
    control_dashboard.display_dashboard()

    # Inicie la simulación en un hilo separado.
    simulation.run()
    control_dashboard.display_dashboard()

    # En algún momento posterior, podrás detener la simulación.
    simulation.stop_simulation()