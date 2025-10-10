from google_play_scraper import app

from .const import VERSION_APP

APP_ID = "org.nativescript.LibreLinkUp"


def get_latest_app_version() -> str:
    try:
        return app(APP_ID)["version"]
    except Exception:
        return VERSION_APP
