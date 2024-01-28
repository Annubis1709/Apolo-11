### Proyecto "Apolo-11" - Simulación de Monitoreo Unificado para Misiones Espaciales

Este proyecto, denominado "Apolo-11", es una simulación desarrollada para la Administración Nacional de la Aeronáutica y el Espacio (NASA), diseñada para llevar a cabo el monitoreo unificado de componentes clave de misiones espaciales. A través de la generación de datos simulados y la creación de informes estadísticos, el programa ofrece una herramienta integral para supervisar y gestionar el estado operativo de satélites, naves espaciales, vehículos espaciales y otros dispositivos utilizados en misiones espaciales.

### Estructura del Proyecto:

El proyecto está organizado en una estructura de directorios que incluye los siguientes componentes principales:

- **apolo-11.py**: Punto de entrada del programa que inicia la simulación y muestra el tablero de control.
- **modules**:
  - **Apolo11Simulation.py**: Contiene la clase `Apolo11Simulation` para simular la generación de datos y ejecutar el ciclo de simulación.
  - **DataGenerator.py**: Contiene la clase `DataGenerator` para generar datos de simulación y almacenar archivos de datos.
  - **FileManager.py**: Contiene la clase `FileManager` para gestionar la movilidad de archivos entre carpetas.
  - **ReportGenerator.py**: Contiene la clase `ReportGenerator` para generar informes estadísticos y el tablero de control.
  - **ControlDashboard.py**: Contiene la clase `ControlDashboard` para mostrar el tablero de control.

### Funcionalidad del Código:

El programa "Apolo-11" realiza las siguientes funciones principales:

1. **Simulación de Datos entre Componentes**: Genera datos de simulación que incluyen información sobre el estado de diferentes dispositivos utilizados en misiones espaciales.
2. **Generación de Archivos y Contenido**: Genera archivos de registro con datos semiestructurados que incluyen fecha, misión, tipo de dispositivo y estado del dispositivo.
3. **Nomenclatura y Generación de Hash**: Utiliza un formato estándar para los nombres de archivo y genera un hash para cada archivo generado.
4. **Generación de Reportes y Manejo de Archivos**: Genera informes estadísticos que incluyen análisis de eventos, gestión de desconexiones, consolidación de misiones y cálculo de porcentajes. Los archivos procesados se mueven a una carpeta de respaldo después de la generación de informes.
5. **Generación de Tablero de Control**: Crea un tablero de control que proporciona una representación visual de los datos relevantes del proceso de simulación.

### Dependencias:

El proyecto "Apolo-11" requiere las siguientes dependencias:

- Python 3.x
- Bibliotecas estándar de Python: `os`, `json`, `random`, `hashlib`, `datetime`, `threading`, `time`, `glob`, `shutil`
- No se requieren bibliotecas de terceros adicionales.

### Configuraciones para Ejecutar con Éxito el Programa:

1. Clonar el repositorio del proyecto desde GitHub: [enlace al repositorio](https://github.com/tu_usuario/apolo-11).
2. Asegurarse de tener instalado Python 3.x en su sistema.
3. Ejecutar el programa utilizando el archivo `apolo-11.py` como punto de entrada.

### Configuraciones Adicionales:

- El programa permite ajustar la periodicidad de la simulación cambiando el parámetro `interval` en la función `start_simulation()` en `Apolo11Simulation.py`.
- Se pueden modificar los rangos de generación de archivos y otros parámetros en `DataGenerator.py` según sea necesario.
- El proyecto incluye un tablero de control que se genera automáticamente y se guarda en formato Markdown en la carpeta de informes.

### Contribuciones y Mejoras:

Se valoran y alientan las contribuciones y mejoras al proyecto "Apolo-11". Si tiene sugerencias, ideas o implementaciones adicionales que puedan agregar valor al proyecto, no dude en colaborar o enviar una solicitud de extracción al repositorio.

Este proyecto es crucial para la NASA y representa una herramienta esencial para el monitoreo y la gestión efectiva de misiones espaciales. Su contribución desempeña un papel fundamental en el éxito de estas trascendentales iniciativas científicas y exploratorias. ¡Gracias por su participación!