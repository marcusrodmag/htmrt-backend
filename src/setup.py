# coding: utf-8
import inspect
import sys
import os
import socket
from flask import Flask, render_template
from flask_api import status
from flask_cors import CORS


def app():

    app = Flask(os.getenv('APP_NAME', __name__))
    app.config.from_object('config.Config')

    # CORS Disabled
    CORS(app)
        
    return app

app = app()

@app.route('/', methods = ['GET'])
def main():
    hostn = socket.gethostname()
    print("hosntame: " + hostn)
    return render_template('main.html', pod_name=hostn, env=env_name())

def env_name():
    return app.config['FLASK_ENV']