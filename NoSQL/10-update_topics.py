#!/usr/bin/env python3
""" updated documentsm"""

def update_topics(mongo_collection, name, topics):
    """ Updates all in a school document  """
    update = mongo_collection.update_many(
            {"name": name},
            {"$set" : {"topics": topics}})
