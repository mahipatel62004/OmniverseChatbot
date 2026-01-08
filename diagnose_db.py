"""
MongoDB Data Diagnostic for OmniVillage
---------------------------------------
✔ Lists all collections
✔ Prints document counts
✔ Shows sample documents (cleaned)
✔ Confirms whether data truly exists
"""

from dotenv import load_dotenv
load_dotenv()

import os
from pymongo import MongoClient
from pprint import pprint

# ---------------- CONFIG ----------------
MONGO_URI = os.environ.get("MONGO_URI")
DB_NAME = os.environ.get("MONGO_DB_NAME", "OmniVillage")

if not MONGO_URI:
    raise RuntimeError("MONGO_URI not found in .env")

# ---------------- CONNECT ----------------
client = MongoClient(MONGO_URI)
db = client[DB_NAME]

print("\n==============================")
print(" OMNIVILLAGE DB DIAGNOSTICS ")
print("==============================\n")

# ---------------- COLLECTION LIST ----------------
collections = db.list_collection_names()
print("📦 Collections found:")
for c in collections:
    print(" -", c)

print("\n------------------------------")

# ---------------- CHECK EACH COLLECTION ----------------
for col_name in sorted(collections):
    col = db[col_name]
    count = col.count_documents({})
    print(f"\n📂 Collection: {col_name}")
    print(f"📊 Document count: {count}")

    if count == 0:
        print("⚠️  EMPTY COLLECTION")
        continue

    print("🔎 Sample documents (max 2):")
    docs = col.find().limit(2)
    for d in docs:
        d.pop("_id", None)
        pprint(d)

print("\n==============================")
print(" DIAGNOSTIC COMPLETE ")
print("==============================\n")
