#!/usr/bin/env python3
"""a Python function that
lists all documents in a collection"""
from typing import List, Dict
from pymongo import MongoClient


def list_all(mongo_collection: MongoClient[Dict[str, any]]) -> List:
    """Functionto list documents from a collection

    Args:
        mongo_collection (pymongo): A mongo object

    Return:
        documents in mongo_collections
        [] if empty
    """
    log = mongo_collection.find()
    if log:
        return log
    return []
