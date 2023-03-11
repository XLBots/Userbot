import time
from datetime import datetime
from pyrogram import filters
from ...import User, command


@User.on_message(command("ping") & filters.me) 
async def _ping(_, message: Message):
    """Ping the assistant"""
    start = time.time()
    semx = await edit_or_reply(message, msg_text="•••••")
    delta_ping = time.time() - start
    await semx.edit(f"**[XL-Userbot]**\n\n• **Ping**: `{delta_ping * 1000:.3f} ms`\n**• , disable_web_page_preview=True) 

   
