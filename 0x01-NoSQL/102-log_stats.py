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
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("{} logs".format(mongo_collection.count_documents({})))
    print("Methods:")
    for i in method:
        print("\tmethod {}: {}".format(i, mongo_collection.count_documents(
            {'method': i})))
    status = mongo_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print("{} status check".format(status))
    top_ips = mongo_collection.aggregate([
        {"$group":
         {
             "_id": "$ip",
             "count": {"$sum": 1}
         }
         },
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
        }}
    ])
    print("IPs:")
    for t in top_ips:
        print(f"\t{t.get('ip')}: {t.get('count')}")


if __name__ == "__main__":
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    main(nginx_collection)
