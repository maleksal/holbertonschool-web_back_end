#!/usr/bin/env python3
"""
Inserts a new document
"""

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """Insert a document."""
    return mongo_collection.insert_one(kwargs).inserted_id
