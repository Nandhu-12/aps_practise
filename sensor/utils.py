import pandas as pd
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.config import mongo_client
import os,sys

"""
    Description: This function return collection as dataframe
    =========================================================
    Params:
    database_name: database name
    collection_name: collection name
    =========================================================
    return Pandas dataframe of a collection
"""

def get_collection_as_dataframe(db_name:str,col_name:str)->pd.DataFrame:
    try:
        logging.info(f"Reading from {db_name} database and {col_name} collection")
        df = pd.DataFrame(list(mongo_client[db_name][col_name].find()))
        logging.info(f"found{df.columns} columns")
        if "_id" in df.columns:
            logging.info(f"Dropping _id column")
            df = df.drop("_id",axis = 1)
        logging.info(f"{df.shape} are rown and columns in the dataframe df")
        return df
    except Exception as e:
        raise SensorException(e,sys)