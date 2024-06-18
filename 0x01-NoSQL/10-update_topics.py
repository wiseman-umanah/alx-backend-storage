#!/usr/bin/env python3
"""a Python function that changes all
topics of a school document based on the name"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """Function to insert documents to a collection

    Args:
        mongo_collection (pymongo): A mongo object
        name (str): name of school
        topic (list): List of topics to add
    """
    old = {"name": name}
    new = {"$set": {"topics": topics}}
    item = mongo_collection.update_one(old, new)
