from pathlib import Path
from github_labeler.utils.custom_logging import logger
from github_labeler.utils.custom_exceptions import CustomJSONError
from github_labeler.core.constants import constants
from github_labeler.core.config import ConfigurationManager
from github_labeler.data.data_ingestion import DataIngestion
# from taxi_fare_prediction.data.data_validation import DataValiadtion
# from taxi_fare_prediction.data.data_preprocessing import DataPreProcessing
# from taxi_fare_prediction.data.data_transformation import DataTransformation


STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_load_config = config.get_data_ingestion_config()
        data_load = DataIngestion(config=data_load_config)
        data_load.download_file()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e