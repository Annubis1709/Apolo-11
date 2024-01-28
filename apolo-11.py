# apolo-11.py
import os
from modules.Apolo11Simulation import Apolo11Simulation
from modules.DataGenerator import DataGenerator
from modules.FileManager import FileManager
from modules.ReportGenerator import ReportGenerator
from modules.ControlDashboard import ControlDashboard

if __name__ == '__main__':
    base_path = os.path.dirname(os.path.abspath(__file__)) # Project root directory
    devices_path = os.path.join(base_path, 'devices')
    backup_path = os.path.join(base_path, 'backups')
    reports_path = os.path.join(base_path, 'reports')

    data_generator = DataGenerator(devices_path)
    file_manager = FileManager(base_path)
    report_generator = ReportGenerator(devices_path, backup_path, reports_path)

    simulation = Apolo11Simulation(data_generator, file_manager, report_generator)

    # Start the simulation in a separate thread.
    simulation.run()

    # At some point later, the simulation can be stopped.
    # simulation.stop_simulation()

    control_dashboard = ControlDashboard(reports_path)
    control_dashboard.display_dashboard()