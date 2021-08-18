#!/usr/bin/env python3
"""
Auth Module.
"""
import bcrypt
from uuid import uuid4
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Takes in a password string arguments and returns bytes.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """return a string representation of a new UUID
    """
    return str(uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """Locating the user by email. If it exists
        """
        try:
            l_user = self._db.find_user_by(email=email)
            valid_user = bcrypt.checkpw(
                password=password.encode('utf-8'),
                hashed_password=l_user.hashed_password)
            return True if valid_user else False
        except NoResultFound:
            return False
