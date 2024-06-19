#!/usr/bin/env python3
""" a Python script that provides some stats
about Nginx logs stored in MongoDB"""
import pymongo


def main(mongo_collection):
    """ Function that provides some stats
    about Nginx logs stored in MongoDB

    Args:
        mongo_collection (pymongo): A mongo object

    """
    client = pymongo.MongoClient()
    collec_nginx = client.logs.nginx

    num_of_docs = collec_nginx.count_documents({})
    print("{} logs".format(num_of_docs))
    print("Methods:")
    methods_list = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods_list:
        method_count = collec_nginx.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, method_count))
    status = collec_nginx.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status))


if __name__ == "__main__":
    main()
