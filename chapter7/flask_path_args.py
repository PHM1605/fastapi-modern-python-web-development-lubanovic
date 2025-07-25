# to test: http http://localhost:5000/hi/Mom
from flask import Flask, jsonify 

app = Flask(__name__)

@app.route("/hi/<who>", methods=["GET"])
def greet(who:str):
    return jsonify(f"Hello? {who}?")

if __name__ == "__main__":
    app.run(debug=True)