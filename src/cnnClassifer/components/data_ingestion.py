import os
from pathlib import Path
import urllib.request as request
import zipfile
from cnnClassifer import logger
from cnnClassifer.entity.config_entity import DataIngestionConfig
from cnnClassifer.utils.common import get_size

# Data Ingestion class with download and unzip the dataset functions defined


class DataIngestion:
    def __init__(self, config: DataIngestionConfig) -> None:
        self.config = config

    def data_size(self):
        logger.info(
            f"Data Set File Size is : {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r')as zip_ref:
            zip_ref.extractall(unzip_path)
