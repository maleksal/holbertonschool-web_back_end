#!/usr/bin/env python3
"""
Log filter Module
"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Returns the log message obfuscated.
    """

    return [

        re.sub(rf"{field}=.*?{separator}",
               f"{field}={redaction}{separator}", message)
        for field in fields
    ][-1]
