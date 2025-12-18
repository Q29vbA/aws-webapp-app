"""
super simple flask web app to get some friction with aws
(+ k3s + argocd + terraform + github actions + aaaaaaaaa)
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def root():
    """Render the home page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
