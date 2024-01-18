from github_labeler.utils.custom_logging import logger
from github_labeler.pipelines.data_pipeline import DataIngestionTrainingPipeline #, DataValidationTrainingPipeline, DataTransformationTrainingPipeline
# from github_labeler.pipelines.model_pipeline import ModelTrainerTrainingPipeline, ModelEvaluationTrainingPipeline
# from github_labeler.modeling.predict_model import PredictionPipeline

import pandas as pd

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_load = DataIngestionTrainingPipeline()
   data_load.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e