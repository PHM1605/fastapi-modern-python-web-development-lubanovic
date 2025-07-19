# to test: http localhost:5000/hi who=Dad
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/hi", methods=["POST"])
def greet():
    who: str = request.json["who"]
    return jsonify(f"Hello? {who}?")

if __name__ == "__main__":
    app.run(debug=True)