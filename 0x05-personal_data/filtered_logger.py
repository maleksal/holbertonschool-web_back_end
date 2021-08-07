#!/usr/bin/env python3
"""
Log filter Module
"""
from typing import List
import logging
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Returns the log message obfuscated.
    """

    for i in fields:

        message = re.sub(rf"{i}=.*?{separator}",
                         f"{i}={redaction}{separator}", message)

    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Log Formatter."""
        return filter_datum(self.fields,
                            self.REDACTION,
                            logging.Formatter(self.FORMAT).format(record),
                            self.SEPARATOR)
