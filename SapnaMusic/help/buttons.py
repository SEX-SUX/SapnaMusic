from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

import config
from SapnaMusic import app

class BUTTONS(object):
    ABUTTON = [
        [
            InlineKeyboardButton("ᴀɪ | ᴄʜᴀᴛɢᴘᴛ", callback_data="AI_BACK HELP_01"),
        ],
        [
            InlineKeyboardButton("ᴄᴀʀʙᴏɴ", callback_data="AI_BACK HELP_02"),
            InlineKeyboardButton("ᴛᴛs", callback_data="AI_BACK HELP_03"),
            InlineKeyboardButton("ɪɴғᴏ", callback_data="AI_BACK HELP_04"),
        ],
        [
            InlineKeyboardButton("ʙᴀɴ", callback_data="AI_BACK HELP_05"),
            InlineKeyboardButton("ᴍᴜᴛᴇ", callback_data="AI_BACK HELP_06"),
            InlineKeyboardButton("ᴋɪᴄᴋ", callback_data="AI_BACK HELP_07"),
        ],
        [
            InlineKeyboardButton("ɢʀᴀᴘʜ", callback_data="AI_BACK HELP_08"),
            InlineKeyboardButton("sɢ", callback_data="AI_BACK HELP_09"),
            InlineKeyboardButton("ᴡᴇʟᴄᴏᴍᴇ", callback_data="AI_BACK HELP_10"),
        ],
        [
            InlineKeyboardButton("ᴢᴏᴍʙɪᴇs", callback_data="AI_BACK HELP_11"),
            InlineKeyboardButton("ɢ-ʙʏᴇ", callback_data="AI_BACK HELP_12"),
            InlineKeyboardButton("ᴍᴀꜱꜱ ᴀᴄᴛɪᴏɴ", callback_data="AI_BACK HELP_13"), 
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ⌯", callback_data=f"settingsback_helper"),]
        ]
