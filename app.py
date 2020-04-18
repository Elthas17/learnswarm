import socket
import os
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    return "IP: {ip}, hostname {h}".format(ip=host_ip, h=host_name)

if __name__ == "__main__":
    app.run('0.0.0.0')