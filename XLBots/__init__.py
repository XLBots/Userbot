# © Xl Userbot // @piroxpower / 2023

import os
import sys
import pathlib
import logging

from pyrogram import Client, filters
from pyromod import listen
from datetime import datetime
from functools import partial
from Python_ARQ import ARQ
from configparser import ConfigParser
from logging.handlers import TimedRotatingFileHandler
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient


# StartTime
StartTime = datetime.now()

# Pyrogram Clients

XlBot = Client(
        "MyAssistant",
        api_id=API_ID,
        api_hash= API_HASH,
        bot_token=TOKEN,
        sleep_threshold=180,
    )
XlBot.start() 

# Skem For Greeting
WELCOME_DELAY_KICK = 60



# Extras
__version__ = "XL.0.1"

# Logging at the start to catch everything From PaperPlane
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.WARNING,
    handlers=[
        TimedRotatingFileHandler(
            "logs/DaisyX.log",
            when="midnight",
            encoding=None,
            delay=False,
            backupCount=10,
        ),
        logging.StreamHandler(),
    ],
)
LOGS = logging.getLogger(__name__)

# Modules Loading From PaperLane
class Userbot(Client):
    file_path = pathlib.Path(__file__).parent
    main_directory = str(file_path.parent)
    def __init__(self, name):
        name = name.lower()

        super().__init__(
            SESSION,# if SESSION is not None else name,
            api_id=API_ID,
            api_hash=API_HASH,
            plugins=dict(root=f"XlBots/plugins"),
            workdir="./",
            app_version="XL.0.1",
        )

    async def start(self):
        await super().start()
        await super().send_message("me", "Xl-Userbot Started 🥳!")

        print("successfully started your X-Userbot! Join @XlChats.")

    async def stop(self, *args):
        await super().stop()
        print("Xl-Userbot Stopped GoodBye.")

# Global Variables
CMD_HELP = {}
client = None
name = "X-Userbot"
ElricX = SkemX(__version__)

# Some Requirements
os.system("pip install --upgrade pip") 
os.system("pip install aiohttps") 
