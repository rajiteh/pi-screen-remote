#!/usr/bin/env python3
from threading import Thread
from flask import Flask, escape, request
from waitress import serve
# from remote import ProjectorRemote
from remote_rf import ProjectorRemoteRF
from paste.translogger import TransLogger

app = Flask(__name__)
remote = ProjectorRemoteRF(17)

@app.route('/stop', methods=["POST"])
def stop():
    remote.stop()
    return {"status": "ok"}

@app.route('/up', methods=["POST"])
def up():
    remote.up()
    return {"status": "ok"}

@app.route('/down', methods=["POST"])
def down():
    timeout = int(request.args.get("timeout", "5"))
    
    thread = Thread(
        target=lambda value: remote.down(value), 
        kwargs={'value': timeout}
    )
    thread.start()
    return {"status": "ok"}

if __name__ == "__main__":
  serve(TransLogger(app), host='0.0.0.0', port=8000)
