import pandas as pd
import pymongo
import os,sys
from dataclasses import dataclass
import json

# Provide the mongodb localhost url to connect python to mongodb.

@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")

env_var = EnvironmentVariable()
#connection establishment
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
TARGET_COLUMN = "class"