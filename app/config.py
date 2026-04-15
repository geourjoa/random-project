import os


class Config:
    DEBUG = os.environ.get("FLASK_DEBUG", "0") == "1"
    DATABASE_PATH = os.environ.get(
        "DATABASE_PATH",
        os.path.join(os.path.dirname(__file__), "pictoria-hikaria-20260326-132606.sqlite"),
    )

