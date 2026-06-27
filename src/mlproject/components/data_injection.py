# Aim to read the data from db after data engineers place it into database
# As of now we'll not connect the database directly, we'll just write the data from source csv directly
# Train test split
# final o/p og this file is to have data in train test split format

import os
import sys
import pandas as pd
from src.mlproject.exception import CustomerException
from src.mlproject.logger import logging
from sklearn.model_selection import train_test_split

# We need to to initiate the input parameters
from dataclasses import dataclass

@dataclass
class DataInjectionConfig: # To save file at folder
    raw_data_path:str = os.path.join('artifacts', 'raw.csv')
    train_data_path:str = os.path.join('artifacts', 'train.csv')
    test_data_path:str = os.path.join('artifacts', 'test.csv')

class DataInjection:
    def __init__(self):
        self.injection_config = DataInjectionConfig() #Here we got all 2 paths inside of the injection_config
    
    def initiate_data_injection(self):
        try:
            logging.info("Entered the data ingestion method")
            # Here if you fetch form the db you first save all the data in one source file, currently I'm skipping
            # Whatever df comes here after reading data we'll save it in raw data path
            os.makedirs(os.path.dirname(self.injection_config.train_data_path), exist_ok=True)

            logging.info("Starting to read the source file")
            df = pd.read_csv("artifacts/Students_data.csv")
            logging.info("Source file read successfully")
            df.to_csv(self.injection_config.raw_data_path)
            logging.info("Initiating train test split")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            logging.info("Train test split completed")
            train_set.to_csv(self.injection_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.injection_config.test_data_path, index=False, header=True)
            logging.info("Train & test data saved successfully")

            return (
                self.injection_config.train_data_path,
                self.injection_config.test_data_path
            )
        
        except Exception as e:
            raise CustomerException(e, sys)
