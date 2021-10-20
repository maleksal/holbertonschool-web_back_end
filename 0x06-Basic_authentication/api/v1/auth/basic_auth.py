#!/usr/bin/env python3
"""
Manage API authentication.
"""
from api.v1.auth.auth import Auth


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
