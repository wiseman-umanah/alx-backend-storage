#!/usr/bin/env python3
"""a Python function that
insert document in a collection"""
from typing import Dict, Any
from pymongo import MongoClient


def insert_school(mongo_collection: MongoClient[Dict[str, any]], **kwargs) -> Any:
    """Function to insert documents to a collection

    Args:
        mongo_collection (pymongo): A mongo object
        kwargs (dict): Dictionary item to insert
    Return:
        insert id
    """
    item = mongo_collection.insert_one(kwargs)
    return item.inserted_id
