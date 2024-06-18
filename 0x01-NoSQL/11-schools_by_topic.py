#!/usr/bin/env python3
"""a Python function that returns the
list of school having a specific topic"""
from typing import List, Dict
from pymongo import MongoClient


def schools_by_topic(mongo_collection: MongoClient[Dict[str, any]], topic: str) -> List:
    """Function to list documents from a collection
    based on topic

    Args:
        mongo_collection (pymongo): A mongo object
        topic (str): the topic

    Return:
        list of schools with topic
    """
    log = mongo_collection.find({"topic": {"$in": [topic]}})
    if log:
        return log
    return []
