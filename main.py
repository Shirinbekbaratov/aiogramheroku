import requests
import os
from aiogram import Bot,Dispatcher,executor,types
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
import logging

from aiogram.utils.executor import start_webhook

from config import BOT_TOKEN

bot=Bot(BOT_TOKEN)

dp=Dispatcher(bot)

WEBHOOK_HOST = f'https://aiogramheroku.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{BOT_TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

WEBAPP_HOST = f'0.0.0.0'
WEBAPP_PORT = os.getenv('PORT',default=8000)

@dp.message_handler(commands=['start','help'])
async def hello_message(message: types.Message):
    user=message.from_user.first_name
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton("👋 Menu")
    btn2 = KeyboardButton("❓ Haqida")
    btn3 = KeyboardButton("Kalkulyator")
    markup.add(btn1, btn2, btn3)
    await message.answer(f'Assalomu alaykum, {user}!'
                        f'\nValyuta narxlari botiga xush kelibsiz!',
                        reply_markup=markup)
@dp.message_handler(content_types=['text'])
async def changevalyut(message: types.Message):
    if(message.text == "❓ Haqida"):
        await message.answer(f"Men sizga valyuta kurslari haqida ma'lumot beruvchi botman."
                             f"Agar bironta valyuta kursi haqida ma'lumot olmoqchi bo'lsangiz"
                             f" Menudan o'zingizga kerakli valyutani tanlang")
    elif(message.text == "👋 Menu"):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = KeyboardButton("Dollar-So'm")
        btn2 = KeyboardButton("Dollar-Rubl")
        btn3 = KeyboardButton("Rubl-So'm")
        back = KeyboardButton("Bosh menuga qaytish")
        markup.add(btn1, btn2, btn3, back)
        await message.answer(text="Menga savollaringiz bormi", reply_markup=markup)

    elif(message.text == "Dollar-So'm"):
        response1=requests.get('https://v6.exchangerate-api.com/v6/9ea72025e6fd3b212e18f573/pair/USD/UZS').json()
        await message.answer(f"1 USD={response1['conversion_rate']} So'm")

    elif(message.text == "Dollar-Rubl"):
        response2=requests.get('https://v6.exchangerate-api.com/v6/9ea72025e6fd3b212e18f573/pair/USD/RUB').json()
        await message.answer(f"1 USD={response2['conversion_rate']} Rubl")
    elif(message.text == "Rubl-So'm"):
        response3=requests.get('https://v6.exchangerate-api.com/v6/9ea72025e6fd3b212e18f573/pair/RUB/UZS').json()
        await message.answer(f"1 Rubl={response3['conversion_rate']} So'm")
    elif (message.text == "Kalkulyator"):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = KeyboardButton("AQSH dollari - So'm")
        btn2 = KeyboardButton("AQSH dollari - Rubl")
        btn3 = KeyboardButton("Rossiya Rubli - So'm")
        back = KeyboardButton("Bosh menuga qaytish")
        markup.add(btn1, btn2, btn3, back)
        await message.answer(text="Iltmos valyutani tanlang", reply_markup=markup)
    elif message.text == "AQSH dollari - So'm":
            await message.answer('Iltimos qiymatni kiriting:')
    #elif int(message.text):
        #response = requests.get('https://v6.exchangerate-api.com/v6/9ea72025e6fd3b212e18f573/pair/RUB/UZS').json()
        #res=response['conversion_rate']
        #ans = int(message.text)*res
        #await message.answer(f"{message.text} AQSH dollari {ans} So'm")

    elif (message.text == "Bosh menuga qaytish"):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = KeyboardButton("👋 Menu")
        button2 = KeyboardButton("❓ Haqida")
        button3 = KeyboardButton("Kalkulyator")
        markup.add(button1, button2, button3)
        await message.answer(text="Bosh sahifaga qaytdingiz", reply_markup=markup)
    else:
        await message.answer(text="Bu buyruqni bajara olmayman")


    #await message.answer('Bajarildi')


async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)

async def on_shutdown(dispatcher):
    await bot.delete_webhook()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )

#if __name__=='__main__':
 #   executor.start_polling(dp,skip_updates=True)
