# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://graph.org/file/07dcf96beca557f37e78c.jpg",
    "https://graph.org/file/02f3b8a4f40f2ce2db693.jpg",
    "https://graph.org/file/b2e13a93a2b8cad24978e.jpg",
    "https://graph.org/file/4f7e3f5cce4c3a178992c.jpg",
    "https://graph.org/file/e780bc4cae78ca6ba3c82.jpg",
    "https://graph.org/file/b8accaf1fc32215a95c8d.jpg",
    "https://graph.org/file/0805fd87e2ef2db8fa652.jpg",
]

HEY_IMG = "https://te.legra.ph/file/098422ced35d8802b27b6.jpg"

ALIVE_ANIMATION = [
    "https://graph.org/file/8f93752bc09d96a7dc599.mp4",
    "https://graph.org/file/5fdc28db1660385c38873.mp4",
    "https://graph.org/file/831ab5e16ee2ff217806e.mp4",
    "https://graph.org/file/e0bd50ce6a2ee2181b4cc.mp4",
    "https://graph.org/file/91220284ae0d2a6779b21.mp4",
    "https://graph.org/file/ed5dda3c26640f7b98a8c.mp4",
    "https://graph.org/file/773d73d8a4be70e8a1e5d.mp4",
    "https://graph.org/file/2f34604a921231d494c47.mp4",
]

FIRST_PART_TEXT = "✨ *ʜᴇʟʟᴏ* `{}` . . ."

PM_START_TEXT = "✨ *ɪ ᴀᴍ TG Manager, ᴀ ɢᴇɴꜱʜɪɴ ɪᴍᴘᴀᴄᴛ ᴛʜᴇᴍᴇᴅ ʀᴏʙᴏᴛ ᴡʜɪᴄʜ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴀɴᴅ ꜱᴇᴄᴜʀᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ʜᴜɢᴇ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ*"

START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="HELP", callback_data="help_back"),
    ],
    [
        InlineKeyboardButton(text="DETAILS", callback_data="Miko_"),
        InlineKeyboardButton(text="AI", callback_data="ai_handler"),
        InlineKeyboardButton(text="SOURCE", callback_data="git_source"),
    ],
    [
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="SUPPORT", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="UPDATES", url="https://t.me/CodeNexus_community"),
        ib(text="SUPPORT", url="https://t.me/Iink_ka_adda"),
    ],
    [
        ib(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
🫧 *Yae-Miko* 🫧

☉ *Here, you will find a list of all the available commands.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
