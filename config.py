import re
import os
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables from .env file (for local dev)
load_dotenv()

# ───── Basic Bot Configuration ───── #
API_ID = int(os.getenv("API_ID", "24196359"))
API_HASH = os.getenv("API_HASH", "20a1b32381ed174799e8af8def3e176b")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

OWNER_ID = int(os.getenv("OWNER_ID", "7404203924"))
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "RDX144")
BOT_USERNAME = os.getenv("BOT_USERNAME", "MOVIE_CLUB_MUSIC_BOT")
BOT_NAME = os.getenv("BOT_NAME", "MyMusicBot")
ASSUSERNAME = os.getenv("ASSUSERNAME", "MC_ASSISTANCE_BOT")
EVALOP = list(map(int, os.getenv("EVALOP", "6797202080").split()))

# ───── Mongo & Logging ───── #
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "mongodb+srv://MovieClub:MovieClub@cluster0.dau2bnj.mongodb.net/MovieClub?retryWrites=true&w=majority&appName=Cluster0")
LOGGER_ID = int(os.getenv("LOGGER_ID", "-1003096094043"))

# ───── Limits and Durations ───── #
RESTART_INTERVAL = int(os.getenv("RESTART_INTERVAL", "86400"))
DURATION_LIMIT_MIN = int(os.getenv("DURATION_LIMIT", "17000"))
SONG_DOWNLOAD_DURATION = int(os.getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(os.getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
TG_AUDIO_FILESIZE_LIMIT = int(os.getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(os.getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))

# ───── Custom API Configs ───── #
API_URL = os.getenv("API_URL", "")
API_KEY = os.getenv("API_KEY", "")
COOKIE_URL = os.getenv("COOKIE_URL", "")
DEEP_API = os.getenv("DEEP_API", "")

# ───── Heroku Configuration ───── #
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME", "")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY", "")

# ───── Git & Updates ───── #
UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "https://github.com/CertifiedCoders/AnnieXMusic")
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = os.getenv("GIT_TOKEN", "")

# ───── Support & Community ───── #
SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/RDX_PVT_GROUP")
SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "https://t.me/RDX_PVT_LTD")

# ───── Assistant Auto Leave ───── #
AUTO_LEAVING_ASSISTANT = os.getenv("AUTO_LEAVING_ASSISTANT", "False").lower() in ["true", "1", "yes"]
AUTO_LEAVE_ASSISTANT_TIME = int(os.getenv("ASSISTANT_LEAVE_TIME", "11500"))

# ───── Error Handling ───── #
DEBUG_IGNORE_LOG = os.getenv("DEBUG_IGNORE_LOG", "True").lower() in ["true", "1", "yes"]

# ───── Spotify Credentials ───── #
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "22b6125bfe224587b722d6815002db2b")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "c9c63c6fbf2f467c8bc68624851e9773")

# ───── Session Strings (supports up to 5 sessions) ───── #
STRING1 = os.getenv("STRING_SESSION", "1BVtsOLABu390WqsaYyUa8paI5GmXawqYdP_ZoLGH9emSRTIR1F4n0BD0oLMYj2qC4dJfXOsYudU9qnB3qsGaYUU6pahrLY3t9WPx7BXfX2VqIH3ne2HW9RBD2-JPSiMdBN-P8sPHm7XEcn7-iRBKY5QC_hTBXdfGJPnRPZV5jt0aXRTIUxZHYJYyVCD3ZZdwstj3SEe8q7yXIRiMsxb7812OgDUu9Hy80jSGsAJiP4Uo02NG0GI_HfF2iqcV59CxXpWgqp9g0et4qC2R9a4YU7kBy5QZuuxKgzrzemsRHNkdlz9pJ9QOFh1_P3i8qTBGuTcVeHfxPBpLRnlitQ-Iq1ZiW4kiPNY=")
STRING2 = os.getenv("STRING2", "")
STRING3 = os.getenv("STRING3", "")
STRING4 = os.getenv("STRING4", "")
STRING5 = os.getenv("STRING5", "")

# ───── Server Settings ───── #
SERVER_PLAYLIST_LIMIT = int(os.getenv("SERVER_PLAYLIST_LIMIT", "3000"))
PLAYLIST_FETCH_LIMIT = int(os.getenv("PLAYLIST_FETCH_LIMIT", "2500"))

# ───── Bot Media Assets ───── #
START_VIDS = [
    "https://telegra.ph/file/9b7e1b820c72a14d90be7.mp4",
    "https://telegra.ph/file/72f349b1386d6d9374a38.mp4",
    "https://telegra.ph/file/a4d90b0cb759b67d68644.mp4"
]

STICKERS = [
    "CAACAgUAAx0Cd6nKUAACASBl_rnalOle6g7qS-ry-aZ1ZpVEnwACgg8AAizLEFfI5wfykoCR4h4E",
    "CAACAgUAAx0Cd6nKUAACATJl_rsEJOsaaPSYGhU7bo7iEwL8AAPMDgACu2PYV8Vb8aT4_HUPHgQ"
]

HELP_IMG_URL = "https://files.catbox.moe/yg2vky.jpg"
PING_VID_URL = "https://files.catbox.moe/3ivvgo.mp4"
PLAYLIST_IMG_URL = "https://telegra.ph/file/94e9eca3b0ec6e2dc6cd5.png"
STATS_VID_URL = "https://telegra.ph/file/e2ab6106ace2e95862372.mp4"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/mlztag.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/tiss2b.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/1d3da7.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/zhymxl.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/veykzq.jpg"
SPOTIFY_ARTIST_IMG_URL = SPOTIFY_ALBUM_IMG_URL = SPOTIFY_PLAYLIST_IMG_URL = YOUTUBE_IMG_URL

# ───── Utility & Functional ───── #
def time_to_seconds(time: str) -> int:
    return sum(int(x) * 60**i for i, x in enumerate(reversed(time.split(":"))))

DURATION_LIMIT = time_to_seconds(f"{int(os.getenv('DURATION_LIMIT', '17000'))}:00")

# ───── Bot Intro Messages ───── #
AYU = ["💞", "🦋", "🔍", "🧪", "⚡️", "🔥", "🎩", "🌈", "🍷", "🥂", "🥃", "🕊️", "🪄", "💌", "🧨"]
AYUV = [
    "ʜᴇʟʟᴏ {0}, 🥀\n\n ɪᴛ'ꜱ ᴍᴇ {1} !\n\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ◆ ꜱᴜᴘᴘᴏʀᴛɪɴɢ ᴘʟᴀᴛꜰᴏʀᴍꜱ : ʏᴏᴜᴛᴜʙᴇ, ꜱᴘᴏᴛɪꜰʏ,\n┠ ◆ ʀᴇꜱꜱᴏ, ᴀᴘᴘʟᴇᴍᴜꜱɪᴄ , ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ ᴇᴛᴄ.\n┗━━━━━━━━━━━━━━━━━⧫\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ➥ Uᴘᴛɪᴍᴇ : {2}\n┠ ➥ SᴇʀᴠᴇʀSᴛᴏʀᴀɢᴇ : {3}\n┠ ➥ CPU Lᴏᴀᴅ : {4}\n┠ ➥ RAM Cᴏɴsᴜᴍᴘᴛɪᴏɴ : {5}\n┠ ➥ ᴜꜱᴇʀꜱ : {6}\n┠ ➥ ᴄʜᴀᴛꜱ : {7}\n┗━━━━━━━━━━━━━━━━━⧫\n\n🫧 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🪽 ➪ [RDX ✔︎](https://t.me/RDX144)"
]

# ───── Runtime Structures ───── #
BANNED_USERS = filters.user()
adminlist, lyrical, votemode, autoclean, confirmer = {}, {}, {}, [], {}

# ───── URL Validation ───── #
if SUPPORT_CHANNEL and not re.match(r"^https?://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHANNEL URL. Must start with https://")

if SUPPORT_CHAT and not re.match(r"^https?://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHAT URL. Must start with https://")
