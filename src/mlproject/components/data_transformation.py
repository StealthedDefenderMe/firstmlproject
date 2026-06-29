import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer #to handle categorical features and missing values
from sklearn.pipeline import Pipeline

from src.mlproject.exception import CustomerException
from src.mlproject.logger import logging
import os

import pickle


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')
    # Whatever model we're gonna use for feature engineering we're saving it pkl file. Above is path

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

# Function for the feature engineering
    def get_data_transformer_obj(self, df):
        # This function is responsible for data transformation
        try:
            # First finding out the numerical and categorical features from dataset
            logging.info("Feature distribution begins")
            num_features = df.select_dtypes(exclude="object").columns
            cat_features = df.select_dtypes(include="object").columns
            logging.info("Feature distribution ends")

            # Numerical Pipeline (specifically for numerical features)
            # Tomorrow what if you get new data and some values are missing in there?.. check below
            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    # SimpleImputer is sklearn functionality where you can replace missing value with a particular strategy
                    ("scaler", StandardScaler())
                    # standard scalar also known as z scalar
                ]
            )

             # Categorical Pipeline
            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    # If cat_features have missing values we replace it with most frequent element or mode
                    ("one_hot_encoder", OneHotEncoder(handle_unknown="ignore")), #Make categorical feature to numerical
                    ('scaler', StandardScaler(with_mean=False))
                    # Scaling here will normalise the all values within same scale
                ]
            )

            logging.info(f"Categorical Columns: {cat_features}")
            logging.info(f"Numerical Columns: {num_features}")

            # Combining both pipelines
            preprocessor = ColumnTransformer(
                transformers=[
                    ("num_pipeline", num_pipeline, num_features),
                    ("cat_pipeline", cat_pipeline, cat_features)
                ]
            )

            return preprocessor
        except Exception as e:
            raise CustomerException(e, sys)
        
    # Below train_path & test_path is data_injection's output
    def initiate_data_transfomation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Reading the train & test file")

            # preprocessing_obj = self.get_data_transformer_obj()
            target_column_name = "math_score"

            # Removing target column from input data
            # Dividing dataset into dependent & independent feature
            input_features_train_df = train_df.drop(columns=target_column_name, axis=1)
            # Assigning target column for training data
            target_feature_train_df = train_df[target_column_name]

            # Dividing the test dataset
            input_feature_test_df = test_df.drop(columns=target_column_name, axis=1)
            target_feature_test_df = test_df[target_column_name]

            preprocessing_obj = self.get_data_transformer_obj(input_features_train_df)

            logging.info("Applying preprocessing on training & testing data")

            input_feature_train_array = preprocessing_obj.fit_transform(input_features_train_df)
            input_feature_test_array = preprocessing_obj.transform(input_feature_test_df)

            # Combining with target column
            train_array = np.c_[
                input_feature_train_array, np.array(target_feature_train_df)
            ]

            test_array = np.c_[
                input_feature_test_array, np.array(target_feature_test_df)
            ]

            self.save_object(file_path = self.data_transformation_config.preprocessor_obj_file_path,
            obj = preprocessing_obj)

            logging.info("Saved preprocessing object")

            return (
                train_array, 
                test_array,
                self.data_transformation_config.preprocessor_obj_file_path
            )

        except Exception as e:
            raise CustomerException(e, sys)
        
    # Function to save pickle file in particular folder location
    def save_object(self, file_path, obj):
        try:
            dir_path = os.path.dirname(file_path)

            os.makedirs(dir_path, exist_ok=True)

            with open(file_path, "wb") as file_obj:
                pickle.dump(obj, file_obj)
        except Exception as e:
            raise CustomerException(e, sys)