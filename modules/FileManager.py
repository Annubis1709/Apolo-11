# modules/FileManager.py

import logging
import os
import shutil


class FileManager:
    """
    Esta clase representa el administrador de archivos de la simulación de Apollo 11.
    Se encarga de mover los archivos procesados a la copia de seguridad.
    """

    def __init__(self, base_path):
        """
        Inicializa el administrador de archivos con la ruta al directorio base.
        Crea los directorios de dispositivos y copias de seguridad si no existen.
        """
        self.base_path = base_path
        self.devices_path = os.path.join(base_path, 'devices')
        self.backup_path = os.path.join(base_path, 'backups')

        # Crea los directorios de dispositivos y copias de seguridad si no existen
        for path in [self.devices_path, self.backup_path]:
            if not os.path.exists(path):
                os.makedirs(path)

    def move_to_backup(self, filename):
        """
        Mueve un archivo procesado al directorio buckups.
        """
        src_path = os.path.join(self.devices_path, filename)
        dst_path = os.path.join(self.backup_path, filename)
        try:
            shutil.move(src_path, dst_path)
        except Exception as e:
            logging.error(f"No se pudo mover el archivo {filename} al directorio backups: {e}")