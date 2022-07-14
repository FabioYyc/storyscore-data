import pymongo
import pandas as pd
from pymongo import MongoClient

def get_db():
    client = MongoClient()
# point the client at mongo URI
    client = MongoClient("mongodb+srv://storypoints-ai-dev:yapShCI5YMxMjxkR@storypointsaicluster0.hivt8.mongodb.net/?retryWrites=true&w=majority")
    #select database
    db = client['issuesDB']
    return db