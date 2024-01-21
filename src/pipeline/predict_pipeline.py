import sys
import os

import pandas as pd
import numpy as np

from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join('artifact', 'model.pkl')
            preprocessor_path = os.path.join('artifact', 'preprocessor.pkl')

            # print("before loading")
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            # print("after loading")
            # print("heres the features ----------------> ", features)
            data_scaled = preprocessor.transform(features)
            # print("after scaling")

            preds = model.predict(data_scaled)
            return preds

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self,
                 gender: str,
                 race_ethnicity: str,
                 parental_level_of_education,
                 lunch: str,
                 test_preparation_course: str,
                 reading_score: int,
                 writing_score: int
                 ):
        self.gender = gender,
        self.race_ethnicity = race_ethnicity,
        self.parental_level_of_education = parental_level_of_education,
        self.lunch = lunch,
        self.test_preparation_course = test_preparation_course,
        self.reading_score = reading_score,
        self.writing_score = writing_score

    def get_data_as_frame(self):
        # the inputs from the front end will get mapped with these values
        # print("reading_score ------------ ", float(''.join(map(str, self.reading_score))),
        #       "writing_score ++++++++++++", self.writing_score)
        try:
            # print("GENDER -> ", self.gender[0])
            custom_data_input_dict = {
                "gender": [self.gender[0]],
                "race_ethnicity": [self.race_ethnicity[0]],
                "parental_level_of_education": [self.parental_level_of_education[0]],
                "lunch": [self.lunch[0]],
                "test_preparation_course": [self.test_preparation_course[0]],
                "reading_score": [float(''.join(map(str, self.reading_score)))],
                "writing_score": [self.writing_score],
            }
            # print("custom data inpu dict **************", custom_data_input_dict)
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e, sys)
