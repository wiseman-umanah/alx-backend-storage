#!/usr/bin/env python3
"""a Python function that
lists all documents in a collection"""
from typing import List, Dict
from pymongo.collection import Collection  # Import Collection from pymongo

def list_all(mongo_collection: Collection) -> List[Dict[str, any]]:
    """
    Function to list all documents from a MongoDB collection.

    Args:
        mongo_collection (Collection): A pymongo Collection object.

    Returns:
        List of documents in the collection.
        Empty list if no documents found.
    """
    return list(mongo_collection.find())

