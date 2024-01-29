# modules/ReportGenerator.py
import datetime
import glob
import json
import os
import shutil


def write_header(dashboard_file, cycle_id):
    """
    Escribe el encabezado del panel de control.
    """
    dashboard_file.write(f"\n# Análisis para Ciclo {cycle_id}\n")


def write_table_header(dashboard_file, headers):
    """
    Escribe el encabezado de una tabla en el panel de control.
    """
    dashboard_file.write(
        "<tr>" + "".join([f"<th style='border: 2px solid black;'>{header}</th>" for header in headers]) + "</tr>\n")


def write_table_row(dashboard_file, row_data):
    """
    Escribe una fila de una tabla en el panel de control.
    """
    dashboard_file.write(
        "<tr>" + "".join([f"<td style='border: 2px solid black;'>{data}</td>" for data in row_data]) + "</tr>\n")


def write_events_analysis(dashboard_file, events_analysis_data):
    """
    Escribe la sección de análisis de eventos del panel de control.
    """
    dashboard_file.write("\n## Análisis de Eventos\n")
    dashboard_file.write(
        "<table style='border-collapse: collapse; border: 2px solid black; text-align: center;'>\n")
    write_table_header(dashboard_file, ["Misión", "Tipo de Dispositivo", "Estado", "Cantidad"])
    for mission, devices in events_analysis_data.items():
        for device_type, state_counts in devices.items():
            for state, count in state_counts.items():
                write_table_row(dashboard_file, [mission, device_type, state, str(count)])
    dashboard_file.write("</table>\n")


def write_disconnection_management(dashboard_file, disconnection_management_data):
    """
    Escribe la sección de gestión de desconexiones del panel de control.
    """
    dashboard_file.write("\n## Gestión de Desconexiones\n")
    dashboard_file.write(
        "<table style='border-collapse: collapse; border: 2px solid black; text-align: center;'>\n")
    write_table_header(dashboard_file, ["Misión", "Tipo de Dispositivo", "Cantidad de Desconexiones"])
    for mission, disconnected_devices in disconnection_management_data.items():
        for device in disconnected_devices:
            write_table_row(dashboard_file, [mission, device['device_type'], str(device['unknown_count'])])
    dashboard_file.write("</table>\n")


def write_consolidation(dashboard_file, consolidation_data):
    """
    Escribe la sección de consolidación de misiones del panel de control.
    """
    dashboard_file.write("\n## Consolidación de Misiones\n")
    dashboard_file.write(
        "<table style='border-collapse: collapse; border: 2px solid black; text-align: center;'>\n")
    write_table_header(dashboard_file, ["Tipo de Dispositivo", "Cantidad de Dispositivos"])
    for device_type, count in consolidation_data.items():
        write_table_row(dashboard_file, [device_type, str(count)])
    dashboard_file.write("</table>\n")


def write_percentages(dashboard_file, percentage_calculation_data):
    """
    Escribe la sección de porcentajes del panel de control.
    """
    dashboard_file.write("\n## Porcentajes\n")
    dashboard_file.write(
        "<table style='border-collapse: collapse; border: 2px solid black; text-align: center;'>\n")
    write_table_header(dashboard_file, ["Misión", "Tipo de Dispositivo", "Estado", "Porcentaje"])
    for mission, devices in percentage_calculation_data.items():
        for device_type, percentage_data in devices.items():
            for state, percentage in percentage_data.items():
                write_table_row(dashboard_file, [mission, device_type, state, f"{percentage:.2f}%"])
    dashboard_file.write("</table>\n")


def generate_html_table(headers, rows):
    """
    Genera una tabla HTML a partir de los encabezados y filas proporcionados.
    """
    html = "<table style='border-collapse: collapse; border: 2px solid black; text-align: center;'>\n"
    html += "<tr>" + "".join(
        [f"<th style='border: 2px solid black;'>{header}</th>" for header in headers]) + "</tr>\n"
    html += "".join([f"<tr>" + "".join(
        [f"<td style='border: 2px solid black;'>{row[i]}</td>" for i in range(len(row))]) + "</tr>\n" for
                     row in rows])
    html += "</table>\n"
    return html


def generate_events_section(data):
    """
    Genera la sección de análisis de eventos del panel de control.
    """
    headers = ["Misión", "Tipo de Dispositivo", "Estado", "Cantidad"]
    rows = [[mission, device_type, state, count] for mission, devices in data.items() for
            device_type, state_counts in devices.items() for state, count in state_counts.items()]
    return generate_html_table(headers, rows)


def generate_disconnection_section(data):
    """
    Genera la sección de gestión de desconexiones del panel de control.
    """
    headers = ["Misión", "Tipo de Dispositivo", "Cantidad de Desconexiones"]
    rows = [[mission, device_type, count] for mission, devices in data.items() for device in devices for
            device_type, count in device.items()]
    return generate_html_table(headers, rows)


def generate_consolidation_section(data):
    """
    Genera la sección de consolidación de misiones del panel de control.
    """
    headers = ["Tipo de Dispositivo", "Cantidad de Dispositivos"]
    rows = [[device_type, count] for device_type, count in data.items()]
    return generate_html_table(headers, rows)


def generate_percentages_section(data):
    """
    Genera la sección de porcentajes del panel de control.
    """
    headers = ["Misión", "Tipo de Dispositivo", "Estado", "Porcentaje"]
    rows = [[mission, device_type, state, percentage] for mission, devices in data.items() for
            device_type, percentages in devices.items() for state, percentage in percentages.items()]
    return generate_html_table(headers, rows)


class ReportGenerator:
    """
    Esta clase representa el generador de informes de la simulación de Apollo 11.
    Se encarga de analizar los eventos, gestionar las desconexiones, consolidar las misiones y calcular los porcentajes.
    """

    def __init__(self, devices_path, backup_path, reports_path):
        """
        Inicializa el generador de informes con las rutas a los directorios de dispositivos, copias de seguridad y
        reportes. Crea los directorios de dispositivos, copias de seguridad y reportes si no existen.
        """
        self.devices_path = devices_path
        self.backup_path = backup_path
        self.reports_path = reports_path

        for path in [self.devices_path, self.backup_path, self.reports_path]:
            if not os.path.exists(path):
                os.makedirs(path)

    @property
    def dashboard_filepath(self):
        """
        Devuelve la ruta al archivo del panel de control.
        """
        return os.path.join(self.reports_path, 'Dashboard.md')  # Tablero de Control de visualizacióón de datos

    def generate_reports(self, cycle_id):
        """
        Genera los informes para un ciclo de simulación.
        """
        # Genera el nombre del archivo de informe estándar
        report_filename = f'APLSTATS-REPORTE-{datetime.datetime.now().strftime("%d%m%y%H%M%S")}.log'

        # Analiza los eventos, gestiona las desconexiones, consolida las misiones y calcula los porcentajes
        analysis_data = self.analyze_and_manage()

        # Guarda el informe
        self.save_report(report_filename, analysis_data)

        # Mueve los archivos procesados a la copia de seguridad (backup)
        self.move_processed_files_to_backup()

        # # Genera el panel de control (dashboard)
        self.generate_dashboard(analysis_data, cycle_id)

    def analyze_and_manage(self):
        """
        Analiza los eventos, gestiona las desconexiones, consolida las misiones y calcula los porcentajes.
        """
        analysis_data = {
            'events_analysis': self.analyze_events(),
            'disconnection_management': self.manage_disconnections(),
            'consolidation': self.consolidate_missions(),
            'percentage_calculation': self.calculate_percentages()}

        return analysis_data

    def analyze_events(self):
        """
        Analiza los eventos de los archivos de log.
        """
        events_analysis_data = {}

        # Obtiene todos los archivos de log generados
        log_files = glob.glob(os.path.join(self.devices_path, '*.log'))

        # Analiza cada archivo de log
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
        """
        Gestiona las desconexiones de los dispositivos.
        """
        disconnection_management_data = {}

        # Llama a la función analyze_events para obtener los datos de análisis de eventos
        events_analysis_data = self.analyze_events()

        # Identifica los dispositivos con un número mayor de estados "desconocido"
        for mission, devices in events_analysis_data.items():
            for device_type, state_counts in devices.items():
                unknown_count = state_counts.get('unknown', 0)

                # Define un umbral para considerar a un dispositivo desconectado
                disconnection_threshold = 1

                if unknown_count > disconnection_threshold:
                    # Registra el dispositivo como teniendo un número mayor de estados "desconocido"
                    if mission not in disconnection_management_data:
                        disconnection_management_data[mission] = []

                    disconnection_management_data[mission].append({
                        'device_type': device_type,
                        'unknown_count': unknown_count
                    })

        return disconnection_management_data

    def consolidate_missions(self):
        """
        Consolida las misiones.
        """
        consolidation_data = {}

        # Llama a la función analyze_events para obtener los datos de análisis de eventos
        events_analysis_data = self.analyze_events()

        # Cuenta el número de dispositivos no operativos en todas las misiones.
        for mission, devices in events_analysis_data.items():
            for device_type, state_counts in devices.items():
                inoperable_count = state_counts.get('killed', 0) + state_counts.get('unknown', 0)

                # Registra el recuento inoperativo para cada tipo de dispositivo en todas las misiones.
                if device_type not in consolidation_data:
                    consolidation_data[device_type] = 0

                consolidation_data[device_type] += inoperable_count

        return consolidation_data

    def calculate_percentages(self):
        """
        Calcula los porcentajes de los datos generados para cada dispositivo y misión.
        """
        percentage_calculation_data = {}

        # Llama a la función analyze_events para obtener los datos de análisis de eventos
        events_analysis_data = self.analyze_events()

        # Calcula los porcentajes de los datos generados para cada dispositivo y misión
        for mission, devices in events_analysis_data.items():
            total_events = sum(sum(device_states.values()) for device_states in devices.values())
            mission_percentage_data = {}
            for device_type, state_counts in devices.items():
                device_percentage_data = {state: (count / total_events) * 100 for state, count in state_counts.items()}
                mission_percentage_data[device_type] = device_percentage_data

            percentage_calculation_data[mission] = mission_percentage_data

        return percentage_calculation_data

    def save_report(self, filename, report_data):
        """
        Guarda el informe generado en un archivo.
        """
        filepath = os.path.join(self.reports_path, filename)
        with open(filepath, 'w') as file:
            json.dump(report_data, file)

    def move_processed_files_to_backup(self):
        """
        Mueve los archivos procesados a la copia de seguridad.
        """
        files_to_move = glob.glob(os.path.join(self.devices_path, '*.log'))
        for file_path in files_to_move:
            filename = os.path.basename(file_path)
            dst_path = os.path.join(self.backup_path, filename)
            shutil.move(file_path, dst_path)

    def generate_dashboard(self, analysis_data, cycle_id):
        """
        Genera el panel de control para el análisis de la simulación.
        """
        dashboard_filename = 'Dashboard.md'
        dashboard_filepath = os.path.join(self.reports_path, dashboard_filename)

        with open(dashboard_filepath, 'a') as dashboard_file:
            write_header(dashboard_file, cycle_id)
            write_events_analysis(dashboard_file, analysis_data['events_analysis'])
            write_disconnection_management(dashboard_file, analysis_data['disconnection_management'])
            write_consolidation(dashboard_file, analysis_data['consolidation'])
            write_percentages(dashboard_file, analysis_data['percentage_calculation'])
