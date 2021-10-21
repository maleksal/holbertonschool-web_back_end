#!/usr/bin/env python3
"""
Manage API authentication.
"""
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar as T
from typing import Tuple
import base64


class BasicAuth(Auth):
    """BasicAuth class.
    """

    def extract_base64_authorization_header(self, auth_header: str) -> str:
        """Returns Base64 of the Authorization header
        """
        if auth_header is None\
                or type(auth_header) != str\
                or not auth_header.startswith("Basic "):
            return None
        return auth_header.split(" ")[1]

    def decode_base64_authorization_header(self, b64_auth_header: str) -> str:
        """Returns decoded value of a Base64 string
        """
        if b64_auth_header is None\
                or type(b64_auth_header) != str:
            return None
        try:
            return base64.b64decode(
                b64_auth_header.encode('ascii')).decode('ascii')
        except Exception as e:
            return None

    def extract_user_credentials(self, db64_auth: str) -> Tuple[str, str]:
        """Returns the user email and password from the B4 decoded value.
        """
        if db64_auth is None\
                or type(db64_auth) != str\
                or ":" not in db64_auth:
            return None, None
        values = db64_auth.split(":")
        return values[0], values[1]

    def user_object_from_credentials(self, ue: str, up: str) -> T('User'):
        """Returns the User instance based on his email and password.
        """
        # ue: user_email
        # up: user_password
        if ue is None or type(ue) != str\
                or up is None or type(up) != str:
            return None
        try:
            users = User.search({'email': ue})
            if users:
                for user in users:
                    if user.is_valid_password(up):
                        return user
        except BaseException:
            return None
        return None
