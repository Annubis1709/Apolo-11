# modules/Apolo11Simulation.py
from random import choice
import threading
import time
import os
import glob

class Apolo11Simulation:
    """
    Esta clase representa la simulación de la misión Apollo 11.
    Utiliza un generador de datos, un administrador de archivos y un generador de reportes.
    También mantiene un estado de ejecución que determina si la simulación está corriendo o no.
    """

    def __init__(self, data_generator, file_manager, report_generator):
        """
        Inicializa la simulación con un generador de datos, un administrador de archivos y un generador de reportes.
        """
        self.data_generator = data_generator
        self.file_manager = file_manager
        self.report_generator = report_generator
        self.running = False

    def start_simulation(self, interval=20):
        """
        Inicia la simulación. Genera datos de log, reportes y mueve los archivos procesados a la copia de seguridad.
        La simulación corre en un ciclo infinito hasta que se llama al método stop_simulation.
        """
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
        """
        Detiene la simulación. Cambia el estado de ejecución a False.
        """
        self.running = False

    def move_processed_files_to_backup(self):
        """
        Mueve los archivos procesados a la copia de seguridad.
        """
        files_to_move = glob.glob(os.path.join(self.data_generator.storage_path, '*.log'))
        for file_path in files_to_move:
            filename = os.path.basename(file_path)
            self.file_manager.move_to_backup(filename)

    def run(self):
        """
        Inicia la simulación en un hilo separado.
        """
        simulation_thread = threading.Thread(target=self.start_simulation)
        simulation_thread.start()
