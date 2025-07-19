# to test: http localhost:5000/hi who:Dad
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/hi", methods=["GET"])
def greet():
    who: str = request.headers.get("who")
    return jsonify(f"Hello? {who}?")

if __name__ == "__main__":
    app.run(debug=True)