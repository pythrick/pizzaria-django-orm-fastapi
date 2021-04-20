from pathlib import Path

from decouple import config
from dj_database_url import parse as db_url

BASE_DIR = Path(__file__).resolve().parent

DEBUG = config("DEBUG", default=False, cast=bool)

SECRET_KEY = config("SECRET_KEY")


DATABASES = {
    "default": config(
        "DATABASE_URL", default=f"sqlite:///{BASE_DIR}/db.sqlite3", cast=db_url
    )
}

INSTALLED_APPS = ["pizzaria"]


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
