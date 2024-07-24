from flask import Flask, jsonify
from grpc_client import get_data_from_db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.get('/api/v1/get_data')
def api_v1_get_data():
    data = get_data_from_db()
    #data = [{"id":"test", "text":"test"}] # > works
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)