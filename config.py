import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_USERNAME = getenv("BOT_USERNAME", "HIMANSHI_MUSIC_BOT")
BOT_TOKEN = getenv("BOT_TOKEN")

MONGO_DB_URI = getenv("MONGO_DB_URI", None)
LOGGER_ID = int(getenv("LOGGER_ID", None))
OWNER_ID = int(getenv("OWNER_ID", None))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv("UPSTREAM_REPO","https://github.com/SEX-SUX/SapnaMusic",)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ALL_SANATANI_BOT")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/SANATANI_SUPPORT")

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "6f3a17d843444c0397ef739342758b46")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "c69244c18a9743bf9fa96efd95dd93f1")

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 2500))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = [
    "https://files.catbox.moe/u7iwi5.jpg",
    "https://files.catbox.moe/rkskww.jpg",
    "https://files.catbox.moe/uz810n.jpg",
    "https://files.catbox.moe/vzl4xb.jpg",
    "https://files.catbox.moe/j2zdsu.jpg",
    "https://files.catbox.moe/nlweex.jpg",
    "https://files.catbox.moe/pp4god.jpg",
    "https://files.catbox.moe/jslln0.jpg",
    "https://files.catbox.moe/fqmdff.jpg",
    "https://files.catbox.moe/eushjw.jpg",
    "https://files.catbox.moe/39fg3k.jpg",
]

PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/4y6acl.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/jrupn9.jpg"
STATS_IMG_URL = "https://files.catbox.moe/jrupn9.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/jrupn9.jpgg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/jrupn9.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/jrupn9.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/jrupn9.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/jrupn9.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/jrupn9.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/jrupn9.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/jrupn9.jpg"


TEMP_DB_FOLDER = "/path/to/temp/db/folder"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
