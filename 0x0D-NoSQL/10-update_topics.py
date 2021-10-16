#!/usr/bin/env python3
"""Changes all topics
"""

from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """Changes topics of a document based on the name """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}})
