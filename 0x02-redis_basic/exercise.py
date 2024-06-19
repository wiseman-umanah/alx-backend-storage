#!/usr/bin/env python3
"""This module shows the use case of
working with Redis in python"""
import redis
import uuid
from typing import Union


class Cache:
    """Base Class that handles all redis methods

    Methods:
        store: stores a new data to a specific key
    """
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, float, int]) -> str:
        """Stores a new data to Redis

        Args:
            data (Any): Data can be a string, float, byte or an int

        Return:
            Returns the key to the data
        """
        key = str(uuid.uuid4())
        (self._redis).mset({key: data})
        return key
