#ChauhanMahesh/Vasusen/DroneBots/COL

from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Basics
API_ID = 4796990
API_HASH = "32b6f41a4bf740efed2d4ce911f145c7"
BOT_TOKEN = "6920047444:AAETLyNHdK9py2Y5nYiJ76ZLR4F6EXjoP_o"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
