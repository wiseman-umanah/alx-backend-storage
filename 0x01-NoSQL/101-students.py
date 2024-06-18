#!/usr/bin/env python3
"""a Python function that
insert document in a collection"""
import pymongo


def top_students(mongo_collection):
    """Function to insert documents to a collection

    Args:
        mongo_collection (pymongo): A mongo object
    Return:
        students with average from peak to lowest
    """
    return mongo_collection.aggregate([
        
        {"$project": {"name": "$name", "averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}}
    ])
