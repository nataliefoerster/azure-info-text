from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Possible Redis connection
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"
        #Possible counter, if you connec to Redis

    html = "<h3>Hello visitor!</h3>" \
           "<b>It is hard to choose between ACI, AKS and OpenShift...</b> <br/>"\
           "<b>But I'm sure you'll find your favourite!</b> <br/>"\
           "<b>Hostname:</b> {hostname}<br/>"
    #html skript
           
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

#Run on Port 8080
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
