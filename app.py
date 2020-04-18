import socket
import os
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    message = 'my first message'
    return "IP: {ip}, hostname {h}, message: {m}".format(ip=host_ip, h=host_name, m=message)

if __name__ == "__main__":
    app.run('0.0.0.0')