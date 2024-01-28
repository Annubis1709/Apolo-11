# apolo-11.py

import os
from modules.Apolo11Simulation import Apolo11Simulation
from modules.DataGenerator import DataGenerator
from modules.FileManager import FileManager
from modules.ReportGenerator import ReportGenerator
from modules.ControlDashboard import ControlDashboard

if __name__ == '__main__':
    """
        Este es el punto de entrada principal para la simulación de Apollo 11.
        Primero, define las rutas para los directorios de dispositivos, respaldos y reportes.
        Luego, crea instancias de los generadores de datos, administrador de archivos y generador de reportes.
        Después, crea una instancia de la simulación de Apollo 11 y la inicia en un hilo separado.
        Finalmente, crea una instancia del panel de control y muestra el panel de control.
        """

    # Define el directorio raíz del proyecto
    base_path = os.path.dirname(os.path.abspath(__file__))

    # Define las rutas para los directorios de devices, buckups y reports
    devices_path = os.path.join(base_path, 'devices')
    backup_path = os.path.join(base_path, 'backups')
    reports_path = os.path.join(base_path, 'reports')

    # Crea instancias de los generadores de datos, administrador de archivos y generador de reportes
    data_generator = DataGenerator(devices_path)
    file_manager = FileManager(base_path)
    report_generator = ReportGenerator(devices_path, backup_path, reports_path)

    # Crea una instancia de la simulación de Apollo 11
    simulation = Apolo11Simulation(data_generator, file_manager, report_generator)

    # Inicia la simulación en un hilo separado
    simulation.run()

    # En algún momento posterior, se podrá detener la simulación
    # simulation.stop_simulation()

    # Crea una instancia del panel de control
    control_dashboard = ControlDashboard(reports_path)

    # Muestra el panel de control
    control_dashboard.display_dashboard()
