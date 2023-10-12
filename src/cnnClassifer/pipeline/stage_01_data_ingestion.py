from cnnClassifer.components.data_ingestion import DataIngestion
from cnnClassifer.config.configuration import ConfigurationManager
from cnnClassifer import logger

# Stage 1 Data Ingestion
STAGE_NAME = "Data Ingestion Stage"

# Pipeline for performing data ingestion task


class DataIngestionTrainingPipleine:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.data_size()
        data_ingestion.extract_zip_file()


# To call Seperatly when required
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipleine()
        obj.main()
        logger.info(
            f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
    except Exception as e:
        logger.exception(e)
        raise e
