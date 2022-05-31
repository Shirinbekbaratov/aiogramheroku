import requests
import os
from aiogram import Bot,Dispatcher,executor,types
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
import logging

BOT_TOKEN='5536336221:AAFCjOmK2FCguf6tGqIkXBYyv8yaTGJ57cw'
APP_URL=''
bot=Bot(BOT_TOKEN)

dp=Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
async def hello_message(message: types.Message):
    user=message.from_user.first_name
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton("👋 Menu")
    btn2 = KeyboardButton("❓ Haqida")
    markup.add(btn1, btn2)
    await message.reply(f'Assalomu alaykum, {user}!'
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
        response=requests.get('https://v6.exchangerate-api.com/v6/9ea72025e6fd3b212e18f573/pair/USD/UZS').json()
        await message.answer(f"1 USD={response['conversion_rate']} So'm")

    elif(message.text == "Dollar-Rubl"):
        response=requests.get('https://v6.exchangerate-api.com/v6/9ea72025e6fd3b212e18f573/pair/USD/RUB').json()
        await message.answer(f"1 USD={response['conversion_rate']} Rubl")
    elif(message.text == "Rubl-So'm"):
        response=requests.get('https://v6.exchangerate-api.com/v6/9ea72025e6fd3b212e18f573/pair/RUB/UZS').json()
        await message.answer(f"1 Rubl={response['conversion_rate']} So'm")

    elif (message.text == "Bosh menuga qaytish"):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = KeyboardButton("👋 Menu")
        button2 = KeyboardButton("❓ Haqida")
        markup.add(button1, button2)
        await message.answer(text="Bosh sahifaga qaytdingiz", reply_markup=markup)
    else:
        await message.answer(text="Bu buyruqni bajara olmayman")

    #await message.answer('Bajarildi')




if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)
