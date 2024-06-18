#!/usr/bin/env python3
"""a Python function that
insert document in a collection"""
from typing import Dict, List
from pymongo import MongoClient


def top_students(mongo_collection: MongoClient[Dict[str, any]]) -> List:
    """Function to insert documents to a collection

    Args:
        mongo_collection (pymongo): A mongo object
    Return:
        students with average from peak to lowest
    """
    return mongo_collection.aggregate([
        {"$unwind": "$topics"},
        {"$group": {"_id": "$_id", "averageScore": { "$avg": "$topics.score" }}},
        {"$project": {"_id": 0, "name": "$_id", "averageScore": 1}},
        {"$sort": {"averageScore": -1}}
        ])


