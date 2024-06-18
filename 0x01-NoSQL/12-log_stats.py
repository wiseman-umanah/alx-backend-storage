#!/usr/bin/env python3
""" a Python script that provides some stats
about Nginx logs stored in MongoDB"""
from typing import List, Dict
from pymongo import MongoClient


def main(mongo_collection: MongoClient[Dict[str, any]]):
    """ Function that provides some stats
    about Nginx logs stored in MongoDB

    Args:
        mongo_collection (pymongo): A mongo object

    """
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("{} logs".format(mongo_collection.count_documents({})))
    print("Methods:")
    for i in method:
        print(f"\tmethod {i}: {mongo_collection.count_documents({"method": i})}")
    print(mongo_collection.count_documents({"path": "/status"}, {"method" : "GET"}), "status check")


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.my_db.nginx
    main(nginx_collection)
