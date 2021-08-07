#!/usr/bin/env python3
"""
Log filter Module
"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, sepereator: str) -> str:
    """ Returns the log message obfuscated.
    """
    return f"{sepereator}".join(re.sub(j.split("=")[1], redaction, j)
                                if j.split('=')[0] in fields else j
                                for j in message.split(sepereator)
                                )
