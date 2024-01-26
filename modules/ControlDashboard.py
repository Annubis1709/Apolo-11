# ControlDashboard.py
import json
import os


class ControlDashboard:
    def __init__(self, report_path):
        self.report_path = report_path

    def display_dashboard(self):
        report_files = [f for f in os.listdir(self.report_path) if f.endswith(".json")]

        if not report_files:
            print("No hay informes disponibles. El tablero está vacío.")
            return

        for report_file in report_files:
            report_filepath = os.path.join(self.report_path, report_file)
            with open(report_filepath, 'r') as file:
                report_data = json.load(file)

            self.create_dashboard(report_data, report_file)

    def create_dashboard(self, data, filename):
        dashboard_filename = f'{filename}_dashboard.txt'
        dashboard_filepath = os.path.join(self.report_path, dashboard_filename)

        with open(dashboard_filepath, 'w') as dashboard_file:
            dashboard_file.write("Dashboard:\n")
            for key, value in data.items():
                dashboard_file.write(f"{key}: {value}\n")
