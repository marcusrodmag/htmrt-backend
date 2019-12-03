# coding: utf-8
from os import path
import os 
import sys
import json

class Config:
    """Set Flask configuration vars from .env file."""

    # General
    TESTING = os.getenv("TESTING", False)
    FLASK_ENV = os.getenv("FLASK_ENV", "production")
    FLASK_DEBUG = os.getenv("FLASK_DEBUG", False)
    CORS_HEADERS = "Content-Type"
    SECRET_KEY = None
    ENV_NAME = os.getenv("ENV_NAME")

    def __init__(self):
        if not self.ENV_NAME:
            raise ValueError("ENV_NAME variable not defined")

    def envname(self):
        return self.ENV_NAME

    def version(self):

        version = None
        if (path.exists("version")):
            with open('version', 'r') as f:
                versionFile = json.load(f)
                try:
                    version = versionFile['version']
                    return version
                except Exception:
                    print ("Invalid version file found")
        return os.getenv('API_VERSION', None)
    
