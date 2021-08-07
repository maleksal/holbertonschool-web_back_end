#!/usr/bin/env python3
"""
Log filter Module
"""
from typing import List
import mysql.connector
import os
import logging
import re


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Returns the log message obfuscated.
    """

    for i in fields:

        message = re.sub(rf"{i}=.*?{separator}",
                         f"{i}={redaction}{separator}", message)

    return message


def get_logger() -> logging.Logger:
    """returns a logging.Logger object"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    stream_handler.RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(stream_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """returns a connector to the database"""
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', "root")
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', "")
    host = os.getenv('PERSONAL_DATA_DB_HOST', "localhost")
    name = os.getenv('PERSONAL_DATA_DB_NAME')
    return mysql.connector.connect(user=username,
                                   password=password,
                                   host=host,
                                   database=name)


def main():
    '''
    takes no arguments and
    returns nothing.
    '''
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    [
        print(c) for r in data for c in r
    ]
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
