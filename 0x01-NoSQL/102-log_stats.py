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

    print("IPs:")

    top_IPs = collec_nginx.aggregate([
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
    for top_ip in top_IPs:
        count = top_ip.get("count")
        ip_address = top_ip.get("ip")
        print("\t{}: {}".format(ip_address, count))


if __name__ == "__main__":
    main()
