#!/usr/bin/env python3
'''Log stats.
'''

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")  # Adjust connection string if needed
db = client["logs"]
collection = db["nginx"]

# Count the total number of logs
total_logs = collection.count_documents({})
print(f"{total_logs} logs")

# Count logs for each method
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for method in methods:
    count = collection.count_documents({"method": method})
    print(f"\tmethod {method}: {count}")

# Count logs with method=GET and path=/status
status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
print(f"{status_check_count} status check")

