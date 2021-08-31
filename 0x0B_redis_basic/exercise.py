#!/usr/bin/env python3
"""
exercise
"""

from typing import Union, Callable, Optional
from functools import wraps
import redis
import uuid


def count_calls(method: Callable) -> Callable:
    """Counts the number of calls of a method."""

    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper """

        self._redis.incr(key)

        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Stores history of I/O of a function.
    """
    cal_k = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        ''' wrapper '''

        self._redis.rpush(f"{cal_k}:inputs", str(args))
        self._redis.rpush(
            f"{cal_k}:outputs", str(args),
            method(self, *args, **kwargs)
        )
        return method(self, *args, **kwargs)
    return wrapper


def replay(fn: Callable) -> str:
    """Displays history of calls.
    """
    thedata = fn.__qualname__

    inputs, outputs = f"{thedata}:inputs", f"{thedata}:outputs"

    redis_ = fn.__self__._redis

    i_redis = redis_.lrange(inputs, 0, -1)

    count = redis_.lrange(outputs, 0, -1)

    Q = fn.__self__._redis.get(thedata).decode('utf-8')

    print(f"{thedata} was called {Q} times:")

    for i, j in zip(i_redis, count):

        print(f"{thedata}(*{i.decode('utf-8')}) -> {j.decode('utf-8')}")


class Cache:
    """Cache class."""

    def __init__(self):
        """Cache constructor."""

        self._redis = redis.Redis()

        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Method stores key."""

        key = str(uuid.uuid4())

        self._redis.set(key, data)

        return key

    def get(self, data: str, fn: Optional[Callable] = None) -> \
            Union[str, bytes, int, float]:
        """Returns the stored data."""

        if data:

            fn_data = self._redis.get(data)
            return fn(fn_data) if fn else fn_data

    def get_str(self, data: bytes) -> str:
        """Parametrize Cache.get."""
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """ parametrize Cache.get."""
        return int(data)
