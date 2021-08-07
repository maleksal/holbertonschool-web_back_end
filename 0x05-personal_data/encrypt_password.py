#!/usr/bin/env python3
"""
password hashing, validation
"""
import bcrypt


def hash_password(password: str) -> bytes:
    '''
    returns a byte string.
    '''
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''
    returns a boolean.
    '''
    return True if bcrypt.checkpw(password.encode('utf-8'), hashed_password) \
        else False
