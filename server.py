from flask import Flask
app = Flask(__name__)

@app.route("/")
def respond():
    return "Server Up"

app.run(host="0.0.0.0")
