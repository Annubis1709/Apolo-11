# Informe de Cumplimiento de Requisitos del Proyecto Apolo-11

## 4.1 Simulación de datos entre componentes

El programa "Apolo-11" cumple con los requisitos especificados de la siguiente manera:

1. **Ubicación del programa**: El programa "Apolo-11" puede ser ubicado en cualquier carpeta de su preferencia. Esto se logra mediante la línea `base_path = os.path.dirname(os.path.abspath(__file__))` en el archivo `apolo-11.py`, que establece la ruta base del proyecto en el directorio donde se encuentra el archivo principal del programa.

2. **Ejecución del programa**: Una vez ubicado en la ruta preferida, el programa se ejecuta correctamente. Esto se hace mediante la línea `if __name__ == '__main__':` en el archivo `apolo-11.py`.

3. **Almacenamiento de información**: Toda la información recopilada durante el proceso de simulación se almacena en la ruta `{ruta_preferencia}/devices`. Esto se logra mediante la definición de `devices_path` en `apolo-11.py` y la utilización de este path para guardar los datos generados en `modules/DataGenerator.py`.

4. **Periodicidad de la ejecución**: La periodicidad de la ejecución se establece inicialmente cada 20 segundos (ciclo de simulación), tal como se indica en el método `start_simulation` de la clase `Apolo11Simulation` en `modules/Apolo11Simulation.py`.

5. **Identificación de archivos generados**: Para cada ciclo de simulación, se generan archivos que están claramente etiquetados para indicar a qué misión corresponden. Esto se realiza en el método `generate_data_log` de la clase `DataGenerator` en `modules/DataGenerator.py`, donde se genera un nombre de archivo único para cada ciclo de simulación que incluye el código de la misión.

## 4.2 Generación de archivos y contenido

El programa "Apolo-11" cumple con los requisitos especificados de la siguiente manera:

1. **Cantidad de archivos generados en cada ejecución**: La cantidad de archivos generados en cada ejecución es aleatoria, inicialmente dentro de un rango que varía desde uno (1) hasta cien (100). Esto se logra mediante la línea `num_files = random.randint(1, 100)` en el método `generate_data_log` de la clase `DataGenerator` en `modules/DataGenerator.py`. Los rangos pueden ser ajustados posteriormente, permitiendo tanto su incremento como su disminución.

2. **Contenido de cada archivo generado**: Cada archivo generado para una misión contiene internamente datos en un formato semiestructurado que incluye los campos: fecha (`date`), misión (`mission`), tipo de dispositivo (`device_type`), estado del dispositivo (`device_status`) y hash. Esto se realiza en el método `generate_data_log` de la clase `DataGenerator` en `modules/DataGenerator.py`, donde se genera un diccionario con estos campos y luego se guarda en un archivo JSON.

## 4.3 Nomenclatura y generación de hash

El programa "Apolo-11" cumple con los requisitos especificados de la siguiente manera:

1. **Estándar de nombres de archivos**: Los nombres de archivo deberán seguir el estándar: `APLSTATS-[REPORTE]-ddmmyyHHMISS.log`. Esto se logra en el método `generate_reports` de la clase `ReportGenerator` en `modules/ReportGenerator.py`, donde se genera el nombre del archivo de informe estándar con el formato especificado.

2. **Generación de hash**: El hash se generará solo si el nombre del archivo no es "unknown" y se calculará a partir de la fecha, la misión, el tipo de dispositivo y el estado del dispositivo. Esto se realiza en el método `generate_data_log` de la clase `DataGenerator` en `modules/DataGenerator.py`, donde se genera un hash SHA256 a partir de estos valores utilizando la función `generate_hash`.

3. **Formato de la fecha**: El formato de la fecha debe seguir la estructura ddmmyyHHMISS (día, mes, año, hora, minuto, segundo) para garantizar la uniformidad y consistencia en los registros de fecha y hora. Esto se logra mediante la línea `timestamp = datetime.datetime.now().strftime("%d%m%y%H%M%S")` en el método `generate_data_log` de la clase `DataGenerator` en `modules/DataGenerator.py`, que genera una cadena de tiempo en el formato especificado.

## 4.4 Generación de reportes, validaciones y manejo de archivos

El programa "Apolo-11" cumple con los requisitos especificados de la siguiente manera:

a) **Estándar de nombres de archivos**: Los nombres de archivo deberán seguir el estándar: `APLSTATS-[REPORTE]-ddmmyyHHMISS.log`. Esto se logra en el método `generate_reports` de la clase `ReportGenerator` en `modules/ReportGenerator.py`, donde se genera el nombre del archivo de informe estándar con el formato especificado.

b) **Análisis de eventos**: Se deberá realizar un análisis de la cantidad de eventos por estado para cada misión y dispositivo. Esto se realiza en el método `analyze_events` de la clase `ReportGenerator` en `modules/ReportGenerator.py`, donde se analizan los eventos de los archivos de log y se cuentan los eventos por estado para cada misión y dispositivo.

c) **Gestión de desconexiones**: Es necesario identificar los dispositivos que presentan un mayor número de desconexiones, específicamente en el estado "unknown", para cada misión. Esto se realiza en el método `manage_disconnections` de la clase `ReportGenerator` en `modules/ReportGenerator.py`, donde se identifican los dispositivos con un número mayor de estados "desconocido".

d) **Consolidación de misiones**: Debe realizarse la consolidación de todas las misiones para determinar cuántos dispositivos son inoperables. Esto se realiza en el método `consolidate_missions` de la clase `ReportGenerator` en `modules/ReportGenerator.py`, donde se consolidan las misiones y se cuenta el número de dispositivos inoperables.

e) **Cálculo de porcentajes**: Se deberá calcular los porcentajes de datos generados para cada dispositivo y misión con respecto a la cantidad total de datos. Esto se realiza en el método `calculate_percentages` de la clase `ReportGenerator` en `modules/ReportGenerator.py`, donde se calculan los porcentajes de los datos generados para cada dispositivo y misión.

f) **Limpieza de archivos**: Una vez generado el informe estadístico, se mueven los archivos que han sido procesados de la carpeta "devices" a una que se llama backups, en la cual quedará almacenado el respaldo del ciclo generado. Esto se logra mediante la función `move_processed_files_to_backup` en la clase `FileManager` en `modules/FileManager.py` y la función `move_processed_files_to_backup` en la clase `Apolo11Simulation` en `modules/Apolo11Simulation.py`.

g) **Generación de tablero de control**: Se desarrolla un archivo que simule un tablero de control. Este archivo proporciona una representación visual que permita a los líderes de otras misiones acceder a datos pertinentes y relevantes del proceso. Esto se logra mediante la función `generate_dashboard` en la clase `ReportGenerator` en `modules/ReportGenerator.py` y la función `create_dashboard` en la clase `ControlDashboard` en `modules/ControlDashboard.py`.

## 5.0 Consideraciones especiales

1. **Portabilidad del proyecto**: Dado que se trata de un proyecto de simulación, es importante tener en cuenta que el proyecto puede ser susceptible de trasladarse o desplegarse en diferentes servidores (computadores). Para garantizar su funcionalidad independientemente de su ubicación, el programa utiliza rutas relativas para almacenar y recuperar archivos, lo que permite que el programa se ejecute correctamente en cualquier servidor sin necesidad de ajustes.

2. **Flexibilidad y escalabilidad**: Los requerimientos relacionados con la generación de datos y su gestión pueden experimentar fluctuaciones, ya sea incremento o decremento. Para adaptar el sistema a estas variaciones sin que sean necesarios cambios sustanciales en el código fuente, el programa utiliza un enfoque modular y basado en plugins. De esta manera, se pueden agregar o eliminar funcionalidades simplemente instalando o desinstalando los plugins correspondientes, sin afectar al resto del sistema.