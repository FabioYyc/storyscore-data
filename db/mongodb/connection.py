from concurrent.futures import process
import pymongo
import pandas as pd
from pymongo import MongoClient
import os
def get_db():
    client = MongoClient()
    database = os.environ['DB_NAME']
# point the client at mongo URI
    client = MongoClient("mongodb+srv://storypoints-ai-dev:yapShCI5YMxMjxkR@storypointsaicluster0.hivt8.mongodb.net/?retryWrites=true&w=majority")
    #select database
    db = client[database]
    return db, client

def close_connection(client: MongoClient):
    client.close()