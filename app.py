import socket
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return f"""
    <h1>Cloud Technologies</h1>
    <p>My first Docker application</p>
    <p>Served by pod: <b>{socket.gethostname()}</b></p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)

