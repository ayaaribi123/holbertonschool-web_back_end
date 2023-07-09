#!/usr/bin/env python3
""" 
Python function that returns the list of school having a specific topic
"""
def schools_by_topic(mongo_collection, topic):
    """
    object topic (string) will be topic searched
    """
    doc = mongo_collection.find({"topics": topic})
    docs = [i for i in doc]
    return docs
