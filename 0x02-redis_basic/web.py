#!/usr/bin/env python3
"""uses the requests module to
obtain the HTML content of a particular URL and returns it."""
import requests
import redis
from typing import Callable
from functools import wraps

res = redis.Redis()


def count_url(method: Callable) -> Callable:
    """Counts url visit wrapper"""
    @wraps(method)
    def wrapper(*args, **kwargs):
        url = args[0]
        cache_key = f"count:{url}"

        res.incr(cache_key)

        result = method(*args, **kwargs)
        res.setex(url, 10, result)
        return result
    return wrapper


@count_url
def get_page(url: str) -> str:
    """Get contents of url

    Args:
        url (str): The url

    Return:
        The content of the url
    """
    r = requests.get(url)
    return r.content


if __name__ == "__main__":
    get_page("http://slowwly.robertomurray.co.uk")
