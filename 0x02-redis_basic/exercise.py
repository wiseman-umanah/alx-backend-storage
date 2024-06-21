#!/usr/bin/env python3
"""This module shows the use case of
working with Redis in python"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def replay(method: Callable) -> None:
    """ display the history call """
    method_key = method.__qualname__
    inputs = method_key + ":inputs"
    outputs = method_key + ":outputs"
    redis = method.__self__._redis
    count = redis.get(method_key).decode("utf-8")
    print("{} was called {} times:".format(method_key, count))
    ListInput = redis.lrange(inputs, 0, -1)
    ListOutput = redis.lrange(outputs, 0, -1)
    allData = list(zip(ListInput, ListOutput))
    for key, data in allData:
        attr, data = key.decode("utf-8"), data.decode("utf-8")
        print("{}(*{}) -> {}".format(method_key, attr, data))


def call_history(method: Callable) -> Callable:
    """History method emulator"""
    method_key = method.__qualname__
    inputs = f"{method_key}:inputs"
    outputs = f"{method_key}:outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapped history call"""
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwds)
        self._redis.rpush(outputs, str(data))
        return data
    return wrapper


def count_calls(method: Callable) -> Callable:
    """ counts method call """
    method_key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapped function """
        self._redis.incr(method_key)
        return method(self, *args, **kwds)
    return wrapper


class Cache:
    """Base Class that handles all redis methods

    Methods:
        store: stores a new data to a specific key
    """
    def __init__(self) -> None:
        """construct the instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores a new data to Redis

        Args:
            data (Any): Data can be a string, float, byte or an int

        Return:
            Returns the key to the data
        """
        key = str(uuid.uuid4())
        (self._redis).mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable]
            = None) -> Union[str, bytes, float, int]:
        """Gets a key and converts it based on fn datatype

        Args:
            key (str): a key string to data
            fn (callable): a callable to the datatype

        Return:
            returns the changed data or the normal return value of Redis
        """
        data = self._redis.get(key)
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, data: str) -> str:
        """Converts data to str UTF-8"""
        return data.decode('utf-8')

    def get_int(self, data: str) -> int:
        """Converts data to int"""
        return int(data)
