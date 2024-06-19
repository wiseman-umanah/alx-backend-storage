#!/usr/bin/env python3
"""a Python function that returns the
list of school having a specific topic"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """Function to list documents from a collection
    based on topic

    Args:
        mongo_collection (pymongo): A mongo object
        topic (str): the topic

    Return:
        list of schools with topic
    """
    return mongo_collection.find({"topics": topic})
