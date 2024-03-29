import os
import zipfile
from src.VehicleTypeDetection.entity.config_entity import DataIngestionConfig
class DataIngestion:
    def __init__(self,config:DataIngestionConfig) -> None:
        self.config=config

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)