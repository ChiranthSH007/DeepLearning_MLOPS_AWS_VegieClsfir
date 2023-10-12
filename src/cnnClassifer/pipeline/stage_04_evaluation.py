from cnnClassifer import logger
from cnnClassifer.components.evaluation import Evaluation
from cnnClassifer.components.prepare_callbacks import PrepareCallback
from cnnClassifer.components.training import Training
from cnnClassifer.config.configuration import ConfigurationManager

STAGE_NAME = "Training"


class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(config=val_config)
        evaluation.evaluation()
        evaluation.save_score()


if __name__ == "__main__":
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
