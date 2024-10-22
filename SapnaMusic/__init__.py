from SapnaMusic.core.bot import Sapna
from SapnaMusic.core.dir import dirr
from SapnaMusic.core.git import git
from SapnaMusic.core.userbot import Userbot
from SapnaMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Sapna()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
