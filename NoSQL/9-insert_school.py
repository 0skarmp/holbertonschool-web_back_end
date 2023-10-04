#!/usr/bin/env python3
"""script to insert"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """scritp to insert documents in collection"""
    result = mongo_collection.insert_one()
    return (result.inserted_id)
