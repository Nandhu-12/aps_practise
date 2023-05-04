import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017")

db_name = "aps"
col_name = "sensor1"
data_file_path = "/config/workspace/aps_failure_training_set1.csv"

if __name__ == "__main__":
    df = pd.read_csv(data_file_path)
    print(f"shape of data: {df.shape}")

    df.reset_index(drop=True,inplace=True)
    records = list(json.loads(df.T.to_json()).values())

    client[db_name][col_name].insert_many(records)


