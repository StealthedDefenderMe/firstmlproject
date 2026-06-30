import sys
from src.mlproject.logger import logging
from src.mlproject.exception import CustomerException
from src.mlproject.components.data_injection import DataInjection
from src.mlproject.components.data_transformation import DataTransformation
from src.mlproject.components.model_trainer import ModelTrainer

if __name__=="__main__": #execution point / means: "Run the code below only when this file is executed directly."
    logging.info("The execution has started")

    try:
        data_injection = DataInjection()

        train_path, test_path = data_injection.initiate_data_injection()

        data_transformation = DataTransformation()

        train_arr, test_arr, preprocessor_path = (
            data_transformation.initiate_data_transfomation(
                train_path,
                test_path
            )
        )

        # Initiating model training code
        model_trainer = ModelTrainer()
        print(model_trainer.initiate_model_training(train_arr, test_arr))

    except Exception as e: #Here exception will capture the error message and sys will contain all lineno, filename
        logging.info("Custome exception occured in app.py")
        raise CustomerException(e, sys)