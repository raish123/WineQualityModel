from src.Wine.Pipelines.data_ingestion_training import DataIngestionTraining
import os,sys
from src.Wine.Exception import CustomException
from src.Wine.loggers import logger
from src.Wine.Pipelines.data_validation_pipeline import DataValidationTraining
from src.Wine.Pipelines.trained_pipeline import ModelTrainingPipeline


stage_name = "Data Ingestion"

try:
    logger.info(f">>>{stage_name} started <<<<")
    #creating an object of DataIngestionTraining class
    dit = DataIngestionTraining()
    dit.main()
    logger.info(f">>>{stage_name} stopped <<<<")

except Exception as e:
    raise CustomException(e,sys)

print()
logger.info("*"*100)


stage_name2 = "Data Validation"

try:
    logger.info(f">>>{stage_name2} started <<<<")
    #creating an object of DataIngestionTraining class
    dvt = DataValidationTraining()
    dvt.main()
    logger.info(f">>>{stage_name2} stopped <<<<")

except Exception as e:
    raise CustomException(e,sys)


print()
logger.info("*"*100)


stage_name3 = "Model training and transformation"

try:
    logger.info(f">>>{stage_name3} started <<<<")
    #creating an object of DataIngestionTraining class
    mtp = ModelTrainingPipeline()
    mtp.main()
    logger.info(f">>>{stage_name3} stopped <<<<")

except Exception as e:
    raise CustomException(e,sys)


