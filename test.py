import datetime
import glob
import json
import os
import shutil

class ReportGenerator:
    def __init__(self, devices_path, backup_path, reports_path):
        self.devices_path = devices_path
        self.backup_path = backup_path
        self.reports_path = reports_path

        for path in [self.devices_path, self.backup_path, self.reports_path]:
            if not os.path.exists(path):
                os.makedirs(path)

    @property
    def dashboard_filepath(self):
        return os.path.join(self.reports_path, 'Dashboard.md') # Changed to Markdown extension

    def generate_reports(self, cycle_id):
        # Generate standard report filename
        report_filename = f'APLSTATS-REPORTE-{datetime.datetime.now().strftime("%d%m%y%H%M%S")}.log'

        # Analyze events, manage disconnections, consolidate missions, calculate percentages
        analysis_data = self.analyze_and_manage()

        # Save the report
        self.save_report(report_filename, analysis_data)

        # Move processed files to backup
        self.move_processed_files_to_backup()

        # Generate dashboard
        self.generate_dashboard(analysis_data, cycle_id)

    def analyze_and_manage(self):
        analysis_data = {
            'events_analysis': self.analyze_events(),
            'disconnection_management': self.manage_disconnections(),
            'consolidation': self.consolidate_missions(),
            'percentage_calculation': self.calculate_percentages()}

        return analysis_data

    def analyze_events(self):
        events_analysis_data = {}

        # Get all generated log files
        log_files = glob.glob(os.path.join(self.devices_path, '*.log'))

        # Get all generated log files
        for log_file in log_files:
            with open(log_file, 'r') as file:
                data = json.load(file)
                mission = data['mission']
                device_type = data['device_type']
                device_status = data['device_status']

                # Initialize the event count for the mission if not present
                if mission not in events_analysis_data:
                    events_analysis_data[mission] = {}

                # Initialize the event count for the device if not present
                if device_type not in events_analysis_data[mission]:
                    events_analysis_data[mission][device_type] = {'excellent': 0, 'good': 0, 'warning': 0, 'faulty': 0,
                                                                  'killed': 0, 'unknown': 0}

                # Increment the count for the specific state.
                events_analysis_data[mission][device_type][device_status] += 1

        return events_analysis_data

    def manage_disconnections(self):
        disconnection_management_data = {}

        # Call the analyze_events function to get event analysis data
        events_analysis_data = self.analyze_events()

        # Identify devices with a higher number of "unknown" states
        for mission, devices in events_analysis_data.items():
            for device_type, state_counts in devices.items():
                unknown_count = state_counts.get('unknown', 0)

                # Define a threshold to consider a device disconnected
                disconnection_threshold = 1

                if unknown_count > disconnection_threshold:
                    # Register the device as having a higher number of "unknown" states
                    if mission not in disconnection_management_data:
                        disconnection_management_data[mission] = []

                    disconnection_management_data[mission].append({
                        'device_type': device_type,
                        'unknown_count': unknown_count
                    })

        return disconnection_management_data

    def consolidate_missions(self):
        consolidation_data = {}

        # Call the analyze_events function to get event analysis data
        events_analysis_data = self.analyze_events()

        # Count the number of non-operational devices in all missions.
        for mission, devices in events_analysis_data.items():
            for device_type, state_counts in devices.items():
                inoperable_count = state_counts.get('killed', 0) + state_counts.get('unknown', 0)

                # Register the inoperative count for each device type in all missions.
                if device_type not in consolidation_data:
                    consolidation_data[device_type] = 0

                consolidation_data[device_type] += inoperable_count

        return consolidation_data

    def calculate_percentages(self):
        percentage_calculation_data = {}

        # Call the analyze_events function to get event analysis data
        events_analysis_data = self.analyze_events()

        # Calculate percentages of data generated for each device and mission
        for mission, devices in events_analysis_data.items():
            for device_type, state_counts in devices.items():
                total_events = sum(state_counts.values())
                percentage_data = {state: count / total_events * 100 for state, count in state_counts.items()}

                # Register the percentage data for each device type in each mission.
                if mission not in percentage_calculation_data:
                    percentage_calculation_data[mission] = {}

                percentage_calculation_data[mission][device_type] = percentage_data

                return percentage_calculation_data

    def save_report(self, filename, report_data):
        filepath = os.path.join(self.reports_path, filename)
        with open(filepath, 'w') as file:
            json.dump(report_data, file)

    def move_processed_files_to_backup(self):
        files_to_move = glob.glob(os.path.join(self.devices_path, '*.log'))
        for file_path in files_to_move:
            filename = os.path.basename(file_path)
            dst_path = os.path.join(self.backup_path, filename)
            shutil.move(file_path, dst_path)

    def generate_dashboard(self, analysis_data, cycle_id):
        dashboard_filename = 'Dashboard.md'
        dashboard_filepath = os.path.join(self.reports_path, dashboard_filename)

        with open(dashboard_filepath, 'a') as dashboard_file:
            dashboard_file.write(f"\n# Análisis para Ciclo {cycle_id}\n")

            sections = [
                ("Análisis de Eventos", self.generate_events_section, analysis_data['events_analysis']),
                ("Gestión de Desconexiones", self.generate_disconnection_section, analysis_data['disconnection_management']),
                ("Consolidación de Misiones", self.generate_consolidation_section, analysis_data['consolidation']),
                ("Porcentajes", self.generate_percentages_section, analysis_data['percentage_calculation'])
            ]

            for title, generate_section, data in sections:
                dashboard_file.write(f"\n## {title}\n")
                dashboard_file.write(generate_section(data))

    def generate_events_section(self, data):
        headers = ["Misión", "Tipo de Dispositivo", "Estado", "Cantidad"]
        rows = [[mission, device_type, state, count] for mission, devices in data.items() for
                device_type, state_counts in devices.items() for state, count in state_counts.items()]
        return self.generate_html_table(headers, rows)

    def generate_disconnection_section(self, data):
        headers = ["Misión", "Tipo de Dispositivo", "Cantidad de Desconexiones"]
        rows = [[mission, device_type, count] for mission, devices in data.items() for device in devices for
                device_type, count in device.items()]
        return self.generate_html_table(headers, rows)

    def generate_consolidation_section(self, data):
        headers = ["Tipo de Dispositivo", "Cantidad de Dispositivos"]
        rows = [[device_type, count] for device_type, count in data.items()]
        return self.generate_html_table(headers, rows)

    def generate_percentages_section(self, data):
        headers = ["Misión", "Tipo de Dispositivo", "Estado", "Porcentaje"]
        rows = [[mission, device_type, state, percentage] for mission, devices in data.items() for
                device_type, percentages in devices.items() for state, percentage in percentages.items()]
        return self.generate_html_table(headers, rows)

    def generate_html_table(self, headers, rows):
        html = "<table style='border-collapse: collapse; border: 2px solid black; text-align: center;'>\n"
        html += "<tr>" + "".join(
            [f"<th style='border: 2px solid black;'>{header}</th>" for header in headers]) + "</tr>\n"
        html += "".join([f"<tr>" + "".join(
            [f"<td style='border: 2px solid black;'>{row[i]}</td>" for i in range(len(row))]) + "</tr>\n" for
                         row in rows])
        html += "</table>\n"
        return html