import json
import os


class ControlDashboard:
    def __init__(self, report_path):
        self.report_path = report_path

    def display_dashboard(self):
        # Este método debe ampliarse para mostrar un panel significativo
        report_files = [f for f in os.listdir(self.report_path) if f.endswith(".json")]

        if not report_files:
            print("No hay informes disponibles. El tablero está vacío.")
            return

        print("Dashboard:")
        for report_file in report_files:
            report_filepath = os.path.join(self.report_path, report_file)
            with open(report_filepath, 'r') as file:
                report_data = json.load(file)

            print(f"Report: {report_file}")
            print("----")
            for key, value in report_data.items():
                print(f"{key}: {value}")
            print("\n")
