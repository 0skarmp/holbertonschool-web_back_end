#!/usr/bin/env python3
"""script to list all document in a collection"""


def list_all(mongo_collection):
    """function to return an empty list"""
    empty_list = []
    collection = mongo_collection.find()
    for document in collection:
        empty_list.append(document)
    return empty_list
