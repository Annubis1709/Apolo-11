import os
import shutil


class FileManager:
    def __init__(self, base_path):
        self.base_path = base_path
        self.devices_path = os.path.join(base_path, 'devices')
        self.backup_path = os.path.join(base_path, 'backups')

        # Crea los directorios devices y backups si no existen
        for path in [self.devices_path, self.backup_path]:
            if not os.path.exists(path):
                os.makedirs(path)

    def move_to_backup(self, filename):
        src_path = os.path.join(self.devices_path, filename)
        dst_path = os.path.join(self.backup_path, filename)
        shutil.move(src_path, dst_path)
