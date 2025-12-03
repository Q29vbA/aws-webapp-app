from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def root():
    """Return a simple health message."""
    return jsonify(message="Hello from aws-webapp-app")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
