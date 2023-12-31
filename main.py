from cnnClassifer import logger
from cnnClassifer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipleine
from cnnClassifer.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifer.pipeline.stage_03_training import ModelTrainingPipeline
from cnnClassifer.pipeline.stage_04_evaluation import ModelEvaluationPipeline

STAGE_NAME = "Data Ingestion stage"

# Performing Stage 1 Task from the created pipeline
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipleine()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model"


try:
    logger.info(f"******************")
    logger.info(f">>>>>> stage {STAGE_NAME}  started <<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(
        f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx===============x")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Training"

try:
    logger.info(f"*****************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(
        f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=============x")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Evaluation"

try:
    logger.info(f"*****************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(
        f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=============x")

except Exception as e:
    logger.exception(e)
    raise e
