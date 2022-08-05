import pandas as pd
import json

from pymongo import InsertOne
def load_dataset(db, conditions= None, limit = 1000) -> pd.DataFrame:
    issuesCollection = db['issues']
    defaultCondition = {
        "storyPoints": {
            "$nin": [None]
        }
    }
    conditions = conditions if conditions is not None else defaultCondition
    issues = pd.DataFrame(list(issuesCollection.find(conditions).limit(limit)))
    return issues

def update_prediction(db, dataset: pd.DataFrame):
    # db = get_db()
    issuesCollection = db['issues']
    for i, row in dataset.iterrows():
        issuesCollection.update_one({'key': row["key"], 
                        'projectId': 
                        row["projectId"]}, 
                        { "$set":{"prediction": row['prediction']}
                            
                        })

def upload_json(db, filename, collection_name):
    collection = db[collection_name]
    requesting = []
    with open(r"%s"% filename) as f:
        for jsonObj in f:
            myDict = json.loads(jsonObj)
            requesting.append(InsertOne(myDict))
    result = collection.bulk_write(requesting)
    