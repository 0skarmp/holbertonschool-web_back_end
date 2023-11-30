#!/usr/bin/env python3
""" Scriptreturn a list of the documents"""


def schools_by_topic(mongo_collection, topic):
    """ returns lists of schools  """
    col = mongo_collection.find({"topics": topic})
    list_school = [doc for doc in col]

    return list_school
