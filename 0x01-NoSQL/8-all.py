#!/usr/bin/env python3
"""a Python function that
lists all documents in a collection"""
import pymongo


def list_all(mongo_collection):
    """
    Function to list all documents from a MongoDB collection.

    Args:
        mongo_collection (Collection): A pymongo Collection object.

    Returns:
        List of documents in the collection.
        Empty list if no documents found.
    """
    return list(mongo_collection.find())
