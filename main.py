from src.Wine.Pipelines.data_ingestion_training import DataIngestionTraining
import os,sys
from src.Wine.Exception import CustomException
from src.Wine.loggers import logger

stage_name = "Data Ingestion"

try:
    logger.info(f">>>{stage_name} started <<<<")
    #creating an object of DataIngestionTraining class
    dit = DataIngestionTraining()
    dit.main()
    logger.info(f">>>{stage_name} stopped <<<<")

except Exception as e:
    raise CustomException(e,sys)
