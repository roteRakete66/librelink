from typing import Final

from google_play_scraper import app

VERSION_APP: Final = "5.2.0"
APP_ID = "org.nativescript.LibreLinkUp"


def get_latest_app_version() -> str:
    try:
        return app(APP_ID)["version"]
    except Exception:  # noqa: BLE001
        return VERSION_APP
