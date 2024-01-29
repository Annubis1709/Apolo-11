# modules/ControlDashboard.py
import json
import os


def generate_html_table(headers, rows):
    """
    Genera una tabla HTML a partir de los encabezados y filas proporcionados.
    """
    html = "<table style='border-collapse: collapse; border: 2px solid black; text-align: center;'>\n"
    html += "<tr>" + "".join(
        [f"<th style='border: 2px solid black;'>{header}</th>" for header in headers]) + "</tr>\n"
    html += "".join([f"<tr>" + "".join(
        [f"<td style='border: 2px solid black;'>{row[i]}</td>" for i in range(len(row))]) + "</tr>\n" for row in
                     rows])
    html += "</table>\n"
    return html


def generate_percentages_section(data):
    """
    Genera la sección de porcentajes del panel de control.
    """
    headers = ["Misión", "Tipo de Dispositivo", "Estado", "Porcentaje"]
    rows = [[mission, device_type, state, percentage] for mission, devices in data.items() for
            device_type, percentages in devices.items() for state, percentage in percentages.items()]
    return generate_html_table(headers, rows)


def generate_consolidation_section(data):
    """
    Genera la sección de consolidación de misiones del panel de control.
    """
    headers = ["Tipo de Dispositivo", "Cantidad de Dispositivos"]
    rows = [[device_type, count] for device_type, count in data.items()]
    return generate_html_table(headers, rows)


def generate_disconnection_section(data):
    """
    Genera la sección de gestión de desconexiones del panel de control.
    """
    headers = ["Misión", "Tipo de Dispositivo", "Cantidad de Desconexiones"]
    rows = [[mission, device_type, count] for mission, devices in data.items() for device in devices for
            device_type, count in device.items()]
    return generate_html_table(headers, rows)


def generate_events_section(data):
    """
    Genera la sección de análisis de eventos del panel de control.
    """
    headers = ["Misión", "Tipo de Dispositivo", "Estado", "Cantidad"]
    rows = [[mission, device_type, state, count] for mission, devices in data.items() for device_type, state_counts
            in devices.items() for state, count in state_counts.items()]
    return generate_html_table(headers, rows)


class ControlDashboard:
    """
    Esta clase representa el panel de control de la simulación de Apollo 11.
    Se encarga de leer los archivos de reporte y generar el panel de control correspondiente.
    """

    def __init__(self, report_path):
        """
        Inicializa el panel de control con la ruta al directorio de reportes.
        """
        self.report_path = report_path

    def display_dashboard(self):
        """
        Muestra el panel de control. Lee todos los archivos de reporte en el directorio de reportes
        y genera un panel de control para cada archivo de reporte.
        """
        report_files = [files for files in os.listdir(self.report_path) if files.endswith(".json")]

        for report_file in report_files:
            report_filepath = os.path.join(self.report_path, report_file)
            with open(report_filepath, 'r') as file:
                report_data = json.load(file)

            self.create_dashboard(report_data, report_file)

    def create_dashboard(self, data, filename):
        """
        Crea un panel de control para los datos del reporte dado.
        """
        dashboard_filename = f'{filename}_dashboard.txt'
        dashboard_filepath = os.path.join(self.report_path, dashboard_filename)

        with open(dashboard_filepath, 'w') as dashboard_file:
            dashboard_file.write("Dashboard:\n")
            for key, value in data.items():
                dashboard_file.write(f"{key}: {value}\n")

    def generate_dashboard(self, analysis_data, cycle_id):
        """
        Genera un panel de control para el análisis de la simulación.
        """
        dashboard_filename = 'Dashboard.md'
        dashboard_filepath = os.path.join(self.report_path, dashboard_filename)

        with open(dashboard_filepath, 'a') as dashboard_file:
            dashboard_file.write(f"\n# Análisis para Ciclo {cycle_id}\n")

            sections = [
                ("Análisis de Eventos", generate_events_section, analysis_data['events_analysis']),
                ("Gestión de Desconexiones", generate_disconnection_section, analysis_data['disconnection_management']),
                ("Consolidación de Misiones", generate_consolidation_section, analysis_data['consolidation']),
                ("Porcentajes", generate_percentages_section, analysis_data['percentage_calculation'])
            ]

            for title, generate_section, data in sections:
                dashboard_file.write(f"\n## {title}\n")
                if title == "Porcentajes":
                    dashboard_file.write(generate_section(data, include_total=True)) # Modificación aquí
                else:
                    dashboard_file.write(generate_section(data))