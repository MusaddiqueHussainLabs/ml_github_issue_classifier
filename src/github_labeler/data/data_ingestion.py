import os
import urllib.request as request
import zipfile
from github_labeler.utils.custom_logging import logger
from github_labeler.utils.helper_functions import get_size
from pathlib import Path
from github_labeler.schemas.config_schema import DataIngestionConfig

class DataIngestion:

    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_url,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")