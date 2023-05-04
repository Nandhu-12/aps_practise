import pandas as pd
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.config import mongo_client
import os,sys
import yaml
import numpy as np
import dill

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

def write_yaml_file(file_path,data:dict):
    try:
        file_dir = os.path.dirname(file_path)
        os.makedirs(file_dir,exist_ok=True)
        with open(file_path,"w") as file_writer:
            yaml.dump(data,file_writer)
    except Exception as e:
        raise SensorException(e, sys)

def convert_columns_float(df:pd.DataFrame,exclude_columns:list)->pd.DataFrame:
    try:
        for column in df.columns:
            if column not in exclude_columns:
                df[column]=df[column].astype('float')
        return df
    except Exception as e:
        raise e