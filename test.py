from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to your Dockerized Flask app!"

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        "message": "Hello from the API",
        "status": "success"
    }
    return jsonify(data)

@app.route('/api/echo', methods=['POST'])
def echo():
    input_data = request.json
    if not input_data:
        return jsonify({"error": "No JSON provided"}), 400
    return jsonify({"received": input_data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
