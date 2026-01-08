from flask import jsonify
def list_sources(vectors_collection):
    # return distinct sources (limit 50)
    srcs = vectors_collection.distinct('source')[:50]
    return srcs
