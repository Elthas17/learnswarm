import socket
import os
from flask import Flask
from datetime import datetime



app = Flask(__name__)


@app.route("/")
def hello():
    # host_name = socket.gethostname()
    # host_ip = socket.gethostbyname(host_name)
    message = 'my second message'
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    return "Message: {m} on {t}".format( m=message, t=now)

if __name__ == "__main__":
    app.run('0.0.0.0')