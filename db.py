from pymongo import MongoClient
from utilities.configuration import config

client = \
    MongoClient('mongodb://{}:{}@ds143030.mlab.com:43030/blogdb'.format(config["DEFAULT"]["DB_USER"],
                                                                        config["DEFAULT"]["DB_PASSWORD"]))
db = client.blogdb


class DBConnection:
    def connect(self, collection):
        return db[collection]
