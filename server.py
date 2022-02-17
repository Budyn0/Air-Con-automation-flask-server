from ast import If
from flask import Flask
import os

app =Flask(__name__)

# memmbers API rout
@app.route("/members")
def members():
    return {"members": ["member1", "member2", "member3"]}

if __name__ == "__main__":
    app.run(debug=True)

