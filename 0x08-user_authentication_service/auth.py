#!/usr/bin/env python3
"""
Auth Module.
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Takes in a password string arguments and returns bytes.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Take mandatory email and password, return a User object.
        """
        try:
            checked_email = self._db.find_user_by(email=email)
            if checked_email:
                raise ValueError(f'User {email} already exists')
        except NoResultFound:
            user = self._db.add_user(email, str(_hash_password(password)))
            return user
