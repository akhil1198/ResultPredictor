# ingesting data from online db or a file

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass  # decorator helps directly define class variable and wouldnt have to use init
class DataIngestionConfig:
    # initialising paths to save data
    train_data_path = str = os.path.join('artifact', 'train.csv')
    test_data_path = str = os.path.join('artifact', 'test.csv')
    raw_data_path = str = os.path.join('artifact', 'raw.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        # write code here to read data from db
        logging.info('Entered Data ingestion method')
        try:
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info('Read the dataset as df')

            os.makedirs(os.path.dirname(
                self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path)

            logging.info("train test split initiated")
            train_set, test_set = train_test_split(
                df, test_size=0.2, random_state=42)

            train_set.to_csv(
                self.ingestion_config.train_data_path, index=False, header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,
                            index=False, header=True)

            logging.info('ingestion completed')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
