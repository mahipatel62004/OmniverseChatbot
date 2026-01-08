@app.route('/api/sources', methods=['GET'])
def list_sources():
    token = request.headers.get('Authorization','').replace('Bearer ','')
    # optional open to demo purposes
    srcs = vectors.distinct('source')[:100]
    return jsonify(srcs)
