#!/usr/bin/env python3
"""
Manage API authentication.
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth class.
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Returns Base64 of the Authorization header
        """
        if authorization_header is None\
                or type(authorization_header) != str\
                or not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ")[1]
