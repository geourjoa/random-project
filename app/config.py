import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "change-me-in-production")
    DEBUG = os.environ.get("FLASK_DEBUG", "0") == "1"

