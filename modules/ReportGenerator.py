# ReportGenerator.py
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

    def generate_reports(self, cycle_id):
        # Generar nombre de archivo de informe estándar
        report_filename = f'APLSTATS-REPORTE-{datetime.datetime.now().strftime("%d%m%y%H%M%S")}.log'

        # Analiza eventos, gestiona desconexiones, consolida misiones, calcula porcentajes
        analysis_data = self.analyze_and_manage()

        # guardar el informe
        self.save_report(report_filename, analysis_data)

        # Mover archivos procesados al backup
        self.move_processed_files_to_backup()

        # Generar dashboard
        self.generate_dashboard(analysis_data, cycle_id)

    def analyze_and_manage(self):
        analysis_data = {'events_analysis': self.analyze_events(),  # a) Analyze events - contar eventos por estado
                         # para cada misión y dispositivo
                         'disconnection_management': self.manage_disconnections(),  # b) Manage disconnections -
                         # identificar dispositivos con un mayor número de "unknown"
                         'consolidation': self.consolidate_missions(),  # c) Consolidate missions - Cuenta los
                         # dispositivos inoperables en todas las misiones
                         'percentage_calculation': self.calculate_percentages()}  # d) Calculate percentages - Calcula
        # porcentajes de datos generados para cada dispositivo y misión

        return analysis_data

    def analyze_events(self):
        events_analysis_data = {}

        # Obtiene todos los archivos log generados
        log_files = glob.glob(os.path.join(self.devices_path, '*.log'))

        # Obtiene todos los archivos log generados
        for log_file in log_files:
            with open(log_file, 'r') as file:
                data = json.load(file)

                mission = data['mission']
                device_type = data['device_type']
                device_status = data['device_status']

                # Inicializa el recuento de eventos para la misión si no está presente
                if mission not in events_analysis_data:
                    events_analysis_data[mission] = {}

                # Inicializa el recuento de eventos para el dispositivo si no está presente
                if device_type not in events_analysis_data[mission]:
                    events_analysis_data[mission][device_type] = {'excellent': 0, 'good': 0, 'warning': 0, 'faulty': 0,
                                                                  'killed': 0, 'unknown': 0}

                # Incrementa el recuento para el estado específico.
                events_analysis_data[mission][device_type][device_status] += 1

        return events_analysis_data

    def manage_disconnections(self):
        disconnection_management_data = {}

        # Llama a la función analyse_events para obtener datos de análisis de eventos
        events_analysis_data = self.analyze_events()

        # Identificar dispositivos con una mayor cantidad de estados "unknown"
        for mission, devices in events_analysis_data.items():
            for device_type, state_counts in devices.items():
                unknown_count = state_counts.get('unknown', 0)

                # Definir un umbral para considerar un dispositivo desconectado
                disconnection_threshold = 10

                if unknown_count > disconnection_threshold:
                    # Registra el dispositivo como si tuviera un mayor número de estados "unknown"
                    if mission not in disconnection_management_data:
                        disconnection_management_data[mission] = []

                    disconnection_management_data[mission].append({
                        'device_type': device_type,
                        'unknown_count': unknown_count
                    })

        return disconnection_management_data

    def consolidate_missions(self):
        consolidation_data = {}

        # Llama a la función analyse_events para obtener datos de análisis de eventos
        events_analysis_data = self.analyze_events()

        # Cuenta los dispositivos inoperables en todas las misiones.
        for mission, devices in events_analysis_data.items():
            for device_type, state_counts in devices.items():
                inoperable_count = state_counts.get('killed', 0) + state_counts.get('unknown', 0)

                # Registra el recuento de inoperativos para cada tipo de dispositivo en todas las misiones.
                if device_type not in consolidation_data:
                    consolidation_data[device_type] = 0

                consolidation_data[device_type] += inoperable_count

        return consolidation_data

    def calculate_percentages(self):
        percentage_calculation_data = {}

        # Llama a la función analyse_events para obtener datos de análisis de eventos
        events_analysis_data = self.analyze_events()

        # Calcula porcentajes de datos generados para cada dispositivo y misión
        for mission, devices in events_analysis_data.items():
            for device_type, state_counts in devices.items():
                total_events = sum(state_counts.values())
                percentage_data = {state: count / total_events * 100 for state, count in state_counts.items()}

                # Registra los datos porcentuales para cada tipo de dispositivo en cada misión.
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

    @property
    def dashboard_filepath(self):
        return os.path.join(self.reports_path, 'Dashboard.txt')

    def generate_dashboard(self, analysis_data, cycle_id):
        with open(self.dashboard_filepath, 'w') as dashboard_file:
            dashboard_file.write("Contenido del panel aquí")
