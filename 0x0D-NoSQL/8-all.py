#!/usr/bin/env python3
""" List documents using Python """

from pymongo import MongoClient


def list_all(mongo_collection):
    """ lists all documents."""
    documents = mongo_collection.find()
    return documents if documents else []
