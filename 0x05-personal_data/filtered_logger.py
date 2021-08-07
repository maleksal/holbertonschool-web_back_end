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

    for i in fields:

        message = re.sub(rf"{i}=.*?{separator}",
                         f"{i}={redaction}{separator}", message)

    return message
