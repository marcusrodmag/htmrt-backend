# coding: utf-8
import inspect
import sys
import os
from flask import Flask
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
def health_check():
    return '', status.HTTP_200_OK

def env_name():
    return app.config['APP_NAME']