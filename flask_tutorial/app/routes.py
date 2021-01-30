from flask import render_template
from app import app
import time

@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Miguel"}
    posts = [
        {
            "author": {"username": "John"},
            "body": "Beautiful day in Portland!"
        },
        {
            "author": {"username": "Susan"},
            "body": "The Avengers movie was so cool!"
        }
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)

# webpage will be hosted on local IP
app.run(host="0.0.0.0", port= 8090)