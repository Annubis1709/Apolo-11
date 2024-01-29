### Proyecto "Apolo-11" - Simulación de Monitoreo Unificado para Misiones Espaciales

Este proyecto, denominado "Apolo-11", es una simulación desarrollada para la Administración Nacional de la Aeronáutica y el Espacio (NASA), diseñada para llevar a cabo el monitoreo unificado de componentes clave de misiones espaciales. A través de la generación de datos simulados y la creación de informes estadísticos, el programa ofrece una herramienta integral para supervisar y gestionar el estado operativo de satélites, naves espaciales, vehículos espaciales y otros dispositivos utilizados en misiones espaciales.

### Estructura del Proyecto:

El proyecto está organizado en una estructura de directorios que incluye los siguientes componentes principales:

```
Apolo-11
├── Apolo-11
│   └── modules
│       ├── __init__.py
│       ├── Apolo11Simulation.py
│       ├── ControlDashboard.py
│       ├── DataGenerator.py
│       ├── FileManager.py
│       └── ReportGenerator.py
└── apolo-11.py
```


- **apolo-11.py**: Punto de entrada del programa que inicia la simulación y muestra el tablero de control.
- **modules**:
  - **Apolo11Simulation.py**: Contiene la clase `Apolo11Simulation` para simular la generación de datos y ejecutar el ciclo de simulación.
  - **DataGenerator.py**: Contiene la clase `DataGenerator` para generar datos de simulación y almacenar archivos de datos.
  - **FileManager.py**: Contiene la clase `FileManager` para gestionar la movilidad de archivos entre carpetas.
  - **ReportGenerator.py**: Contiene la clase `ReportGenerator` para generar informes estadísticos y el tablero de control.
  - **ControlDashboard.py**: Contiene la clase `ControlDashboard` para mostrar el tablero de control.

A continuación se presenta una breve descripción de lo que hace cada clase:

1. Clase `Apolo11Simulation`: Esta clase maneja la simulación misma. Genera registros de datos, mueve archivos procesados (directorio reports) al directorio buckups y ejecuta la simulación en un hilo separado. La simulación puede detenerse en cualquier momento.

2. Clase `DataGenerator`: Esta clase genera registros de datos. Selecciona aleatoriamente un tipo de dispositivo y un estado de dispositivo, y crea un hash único para cada entrada de registro.

3. Clase `FileManager`: Esta clase maneja el movimiento de archivos de un directorio a otro. Puede mover archivos del directorio de devices al directorio de buckups.

4. Clase `ReportGenerator`: Esta clase genera informes basados en los registros de datos generados. Analiza eventos, gestiona desconexiones, consolida misiones y calcula porcentajes. También guarda los informes y mueve archivos procesados a buckups.

5. Clase `ControlDashboard`: Esta clase muestra el panel de control. Lee los archivos de informe y crea un panel de control (Dashboard.md) basado en los datos del informe.

Flujo simplificado de cómo interactúan estos componentes:

1. El script principal (`apolo-11.py`) inicializa instancias de `DataGenerator`, `FileManager`, `ReportGenerator` y `ControlDashboard`. Estas instancias se pasan a la instancia de `Apolo11Simulation`.

2. La instancia de `Apolo11Simulation` inicia la simulación en un hilo separado. Durante la simulación, genera registros de datos, genera informes y mueve archivos procesados a la carpeta buckups.

3. Una vez iniciada la simulación, se muestra la instancia de `ControlDashboard`. Lee los archivos de informe y crea un panel de control (Dashboard.md) basado en los datos del informe.

Este código utiliza subprocesamiento múltiple, donde la simulación se ejecuta en un hilo separado del script principal. Esto permite que la simulación se ejecute simultáneamente con el resto del programa, haciendo que el programa sea más receptivo y eficiente.

### Funcionalidad del Código:

El programa "Apolo-11" realiza las siguientes funciones principales:

1. **Simulación de Datos entre Componentes**: Genera datos de simulación que incluyen información sobre el estado de diferentes dispositivos utilizados en misiones espaciales.
2. **Generación de Archivos y Contenido**: Genera archivos de registro con datos semiestructurados que incluyen fecha, misión, tipo de dispositivo y estado del dispositivo.
3. **Nomenclatura y Generación de Hash**: Utiliza un formato estándar para los nombres de archivo y genera un hash para cada archivo generado.
4. **Generación de Reportes y Manejo de Archivos**: Genera informes estadísticos que incluyen análisis de eventos, gestión de desconexiones, consolidación de misiones y cálculo de porcentajes. Los archivos procesados se mueven a una carpeta de buckups después de la generación de informes.
5. **Generación de Tablero de Control**: Crea un tablero de control (Dashboard.md) que proporciona una representación visual de los datos relevantes del proceso de simulación.

### Dependencias:

El proyecto "Apolo-11" requiere las siguientes dependencias:

- Python 3.x
- Bibliotecas estándar de Python: `os`, `json`, `random`, `hashlib`, `datetime`, `threading`, `time`, `glob`, `shutil`
- No se requieren bibliotecas de terceros adicionales.


1. **Python**: El lenguaje de programación utilizado para escribir todo el código.

2. **Módulo `os`**: Este módulo proporciona funciones para interactuar con el sistema operativo, como obtener rutas de archivos y directorios. Se utiliza en el código para definir las rutas de los archivos de dispositivos, respaldos y informes.

3. **Módulo `random`**: Este módulo proporciona funciones para generar números pseudoaleatorios. Se utiliza en el código para seleccionar aleatoriamente los códigos de misión y los estados de los dispositivos.

4. **Módulo `time`**: Este módulo proporciona funciones relacionadas con el tiempo, como la espera de un intervalo de tiempo. Se utiliza en el código para hacer que la simulación se ejecute durante un período de tiempo determinado.

5. **Módulo `threading`**: Este módulo proporciona una API de alto nivel para trabajar con hilos. Se utiliza en el código para ejecutar la simulación en un hilo separado, permitiendo que la simulación se ejecute en paralelo con el resto del programa.

6. **Módulo `logging`**: Este módulo proporciona una API para registrar mensajes de eventos. Se utiliza en el código para registrar errores cuando no se puede mover un archivo al directorio de respaldo.

7. **Módulo `json`**: Este módulo proporciona funciones para trabajar con JSON. Se utiliza en el código para guardar y cargar datos de los registros de datos y los informes.

8. **Módulo `shutil`**: Este módulo proporciona funciones de alto nivel para copiar y eliminar archivos. Se utiliza en el código para mover archivos de un directorio a otro.

9. **Módulo `glob`**: Este módulo proporciona funciones para encontrar rutas de archivos y directorios que coinciden con patrones específicos. Se utiliza en el código para encontrar archivos de registro para moverlos al directorio de respaldo.
### Configuraciones para Ejecutar con Éxito el Programa:

1. Clonar el repositorio del proyecto desde GitHub: [enlace al repositorio](https://github.com/Annubis1709/apolo-11).
2. Asegurarse de tener instalado Python 3.x en su sistema.
3. Ejecutar el programa utilizando el archivo `apolo-11.py` como punto de entrada.

### Configuraciones Adicionales:

- El programa permite ajustar la periodicidad de la simulación cambiando el parámetro `interval` en la función `start_simulation()` en `Apolo11Simulation.py`.
- Se pueden modificar los rangos de generación de archivos y otros parámetros en `DataGenerator.py` según sea necesario.
- El proyecto incluye un tablero de control que se genera automáticamente y se guarda en formato Markdown en la carpeta de reports.

## ¿Cómo se manejan los errores y excepciones en el código?
En el código proporcionado, se manejan los errores y excepciones principalmente a través del uso de bloques `try`/`except`. Este es un patrón común en Python para capturar y manejar excepciones que pueden surgir durante la ejecución del programa.

Por ejemplo, en la clase `FileManager`, hay un método llamado `move_to_backup` que intenta mover un archivo a un directorio de respaldo. Si ocurre un error durante este proceso (por ejemplo, si el archivo no existe o si no se tiene permiso para moverlo), se captura la excepción y se registra un mensaje de error utilizando el módulo `logging`.

```python
def move_to_backup(self, filename):
    src_path = os.path.join(self.devices_path, filename)
    dst_path = os.path.join(self.backup_path, filename)
    try:
        shutil.move(src_path, dst_path)
    except Exception as e:
        logging.error(f"No se pudo mover el archivo {filename} al directorio backup: {e}")
```

En este código, `shutil.move(src_path, dst_path)` es el bloque de código dentro del bloque `try`. Si ocurre una excepción durante la ejecución de este bloque de código, la ejecución del programa se traslada al bloque `except` correspondiente. En este caso, la excepción se registra y se continúa con la ejecución normal del programa.

Además, en la clase `DataGenerator`, se utiliza la función `open()` dentro de un bloque `try` para abrir un archivo. Si ocurre un error al intentar abrir el archivo (por ejemplo, si el archivo no existe), se captura la excepción y se registra un mensaje de error.

```python
def save_data(self, filename, data):
    filepath = os.path.join(self.storage_path, filename)
    try:
        with open(filepath, 'w') as file:
            json.dump(data, file)
    except Exception as e:
        logging.error(f"Error al guardar los datos: {e}")
```

En resumen, este código utiliza bloques `try`/`except` para manejar las excepciones que pueden surgir durante la ejecución del programa. Cuando ocurre una excepción, se registra un mensaje de error y se continúa con la ejecución normal del programa
### Contribuciones y Mejoras:

Se valoran y alientan las contribuciones y mejoras al proyecto "Apolo-11". Si tiene sugerencias, ideas o implementaciones adicionales que puedan agregar valor al proyecto, no dude en colaborar o enviar una solicitud de extracción al repositorio.