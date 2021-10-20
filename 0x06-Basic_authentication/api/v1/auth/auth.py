#!/usr/bin/env python3
"""
Manage API authentication.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Manage API authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns False.
        """
        if path is None or not excluded_paths or not excluded_paths:
            return True
        path += '/' if not path.endswith('/') else ''
        return not (path in excluded_paths)

    def authorization_header(self, request=None) -> str:
        """Returns None - request will be the Flask request object
        """
        if request is None:
            return None
        if not request.headers.get("Authorization"):
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns None - request will be the Flask request object
        """
        return None


class BasicAuth(Auth):
    """BasicAuth class.
    """
