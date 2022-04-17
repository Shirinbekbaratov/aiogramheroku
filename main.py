import os
from aiogram import Bot,Dispatcher,types
import logging

BOT_TOKEN=''
APP_URL=''
bot=Bot(BOT_TOKEN)

dp=Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message):
    await message.reply('Hi')
