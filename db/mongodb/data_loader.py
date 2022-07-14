import pandas as pd

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