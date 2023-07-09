#!/usr/bin/env python3
""" 
Python function that inserts a new document in a
collection based on kwarg
"""


def insert_school(mongo_collection, **kwargs):
    """
    Returns the new _id
    """
    doc_id = mongo_collection.insert(kwargs)
    return doc_id
