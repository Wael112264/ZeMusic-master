import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["باشه","المبرمج","مبرمج السورس","المالك"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/522d508e2bcb1db660111.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[الـبـاشـة ](https://t.me/MG4_44)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @MG4_44 ❫
◉ 𝙸𝙳      : ❪ `6425347654` ❫
◉ 𝙱𝙸𝙾    : ❪.❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒الـبـاشـة", url=f"https://t.me/MG4_44"), 
                 ],[
                   InlineKeyboardButton(
                        "قناة السورس", url=f"https://t.me/G_aE5"),
                ],

            ]

        ),

    )
