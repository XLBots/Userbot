import config
from pyrogram import filters

PREFIX = config.CMD_HNDLR

# Command Handler
command = partial(filters.command, prefixes=PREFIX)
