import asyncio
import traceback

from pyrogram.types import Message
from pyrogram import filters, __version__ as pyrover
from pytgcalls import (__version__ as pytgver)

from NIXA.main import bot as Client
from NIXA.filters import command
from NIXA.decorators import sudo_users_only
from NIXA.Database.dbchat import get_served_chats
from NIXA.Database.dbusers import get_served_users
from NIXA.Database.dbpunish import get_gbans_count

from config import BOT_USERNAME


@Client.on_message(command(["broadcast", f"broadcast@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def broadcast_message_nopin(c: Client, message: Message):
    if not message.reply_to_message:
        pass
    else:
        x = message.reply_to_message.message_id
        y = message.chat.id
        sent = 0
        chats = []
        schats = await get_served_chats()
        for chat in schats:
            chats.append(int(chat["chat_id"]))
        for i in chats:
            try:
                m = await c.forward_messages(i, y, x)
                await asyncio.sleep(0.3)
                sent += 1
            except Exception:
                pass
        await message.reply_text(f"✅ ʙʀᴏᴀᴅᴄᴀsᴛ ᴄᴏᴍᴘʟᴇᴛᴇ ɪɴ {sent} ɢʀᴏᴜᴘ.")
        return
    if len(message.command) < 2:
        await message.reply_text(
            "**» ᴜsᴀɢᴇ**:\n\n/broadcast (`ᴍᴇssᴀɢᴇ`) ᴏʀ (`ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ`)"
        )
        return
    text = message.text.split(None, 1)[1]
    sent = 0
    chats = []
    schats = await get_served_chats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    for i in chats:
        try:
            m = await c.send_message(i, text=text)
            await asyncio.sleep(0.3)
            sent += 1
        except Exception:
            pass
    await message.reply_text(f"✅ ʙʀᴏᴀᴅᴄᴀsᴛ ᴄᴏᴍᴘʟᴇᴛᴇ ɪɴ {sent} ɢʀᴏᴜᴘ.")


@Client.on_message(command(["broadcast_pin", f"broadcast_pin@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def broadcast_message_pin(c: Client, message: Message):
    if not message.reply_to_message:
        pass
    else:
        x = message.reply_to_message.message_id
        y = message.chat.id
        sent = 0
        pin = 0
        chats = []
        schats = await get_served_chats()
        for chat in schats:
            chats.append(int(chat["chat_id"]))
        for i in chats:
            try:
                m = await c.forward_messages(i, y, x)
                try:
                    await m.pin(disable_notification=True)
                    pin += 1
                except Exception:
                    pass
                await asyncio.sleep(0.3)
                sent += 1
            except Exception:
                pass
        await message.reply_text(
            f"✅ ʙʀᴀᴏᴅᴄᴀsᴛ ᴄᴏᴍᴘʟᴇᴛᴇ ɪɴ {sent} ɢʀᴏᴜᴘ.\n📌 sᴇɴᴛ ᴡɪᴛʜ {pin} ᴄʜᴀᴛ ᴘɪɴs."
        )
        return
    if len(message.command) < 2:
        await message.reply_text(
            "**» ᴜsᴀɢᴇ**:\n\n/broadcast_pin (`ᴍᴇssᴀɢᴇ`) or (`ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ`)"
        )
        return
    text = message.text.split(None, 1)[1]
    sent = 0
    pin = 0
    chats = []
    schats = await get_served_chats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    for i in chats:
        try:
            m = await c.send_message(i, text=text)
            try:
                await m.pin(disable_notification=True)
                pin += 1
            except Exception:
                pass
            await asyncio.sleep(0.3)
            sent += 1
        except Exception:
            pass
    await message.reply_text(
        f"✅ ʙʀᴏᴀᴅᴄᴀsᴛ ᴄᴏᴍᴘʟᴇᴛᴇ ɪɴ {sent} ɢʀᴏᴜᴘ.\n📌 sᴇɴᴛ ᴡɪᴛʜ {pin} ᴄʜᴀᴛ ᴘɪɴs."
    )
