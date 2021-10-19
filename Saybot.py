from telebot import types
import telebot
import gtts
import datetime
import os
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


current_path = os.path.abspath(os.getcwd()) 
token = '2082423455:AAFGDESlhAY-OjQeBWA55t0oUVDaeyZ3Oco'

# text = ''
# say = gtts.gTTS(text, lang='ru', slow=False)
# say.save('output1.mp3')

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def say_hello(message):
    bot.send_message(message.chat.id, "Hello, i'm speech synthesizer!")

@bot.message_handler(commands=['alphabet'])
def alphabet(message):
    markup = types.ReplyKeyboardMarkup()
    buttonA = types.KeyboardButton('A')
    buttonB = types.KeyboardButton('B')
    buttonC = types.KeyboardButton('C')
    buttonD = types.KeyboardButton('D')
    buttonE = types.KeyboardButton('E')
    buttonF = types.KeyboardButton('F')
    buttonG = types.KeyboardButton('G')
    buttonH = types.KeyboardButton('H')
    buttonI = types.KeyboardButton('I')
    buttonJ = types.KeyboardButton('J')
    buttonK = types.KeyboardButton('K')
    buttonL = types.KeyboardButton('L')
    buttonM = types.KeyboardButton('M')
    buttonN = types.KeyboardButton('N')
    buttonO = types.KeyboardButton('O')
    buttonP = types.KeyboardButton('P')
    buttonQ = types.KeyboardButton('Q')
    buttonR = types.KeyboardButton('R')
    buttonS = types.KeyboardButton('S')
    buttonT = types.KeyboardButton('T')
    buttonU = types.KeyboardButton('U')
    buttonV = types.KeyboardButton('V')
    buttonW = types.KeyboardButton('W')
    buttonX = types.KeyboardButton('X')
    buttonY = types.KeyboardButton('Y')
    buttonZ = types.KeyboardButton('Z')

    markup.row(buttonQ,buttonW,buttonE,buttonR,buttonT,buttonY,buttonU,buttonI,buttonO,buttonP,)
    markup.row(buttonA,buttonS,buttonD,buttonF,buttonG,buttonH,buttonJ,buttonK,buttonL)
    markup.row(buttonZ,buttonX,buttonC,buttonV,buttonB,buttonN,buttonM,)
    bot.send_message(message.chat.id, 'working',reply_markup=markup)

@bot.message_handler(commands=['alphabet2'])
def alphabet2(message):
    markup2 = types.InlineKeyboardMarkup()
    buttonA = types.InlineKeyboardButton('A', callback_data = 'a')
    buttonB = types.InlineKeyboardButton('B', callback_data = 'b')
    buttonC = types.InlineKeyboardButton('C', callback_data = 'c')
    buttonD = types.InlineKeyboardButton('D', callback_data = 'd')
    buttonE = types.InlineKeyboardButton('E', callback_data = 'e')
    buttonF = types.InlineKeyboardButton('F', callback_data = 'f')
    buttonG = types.InlineKeyboardButton('G', callback_data = 'g')
    buttonH = types.InlineKeyboardButton('H', callback_data = 'h')
    buttonI = types.InlineKeyboardButton('I', callback_data = 'i')
    buttonJ = types.InlineKeyboardButton('J', callback_data = 'j')
    buttonK = types.InlineKeyboardButton('K', callback_data = 'k')
    buttonL = types.InlineKeyboardButton('L', callback_data = 'l')
    buttonM = types.InlineKeyboardButton('M', callback_data = 'm')
    buttonN = types.InlineKeyboardButton('N', callback_data = 'n')
    buttonO = types.InlineKeyboardButton('O', callback_data = 'o')
    buttonP = types.InlineKeyboardButton('P', callback_data = 'p')
    buttonQ = types.InlineKeyboardButton('Q', callback_data = 'q')
    buttonR = types.InlineKeyboardButton('R', callback_data = 'r')
    buttonS = types.InlineKeyboardButton('S', callback_data = 's')
    buttonT = types.InlineKeyboardButton('T', callback_data = 't')
    buttonU = types.InlineKeyboardButton('U', callback_data = 'u')
    buttonV = types.InlineKeyboardButton('V', callback_data = 'v')
    buttonW = types.InlineKeyboardButton('W', callback_data = 'w')
    buttonX = types.InlineKeyboardButton('X', callback_data = 'x')
    buttonY = types.InlineKeyboardButton('Y', callback_data = 'y')
    buttonZ = types.InlineKeyboardButton('Z', callback_data = 'z')
    markup2.row(buttonQ,buttonW,buttonE,buttonR,buttonT,buttonY,buttonU,buttonI,buttonO,buttonP,)
    markup2.row(buttonA,buttonS,buttonD,buttonF,buttonG,buttonH,buttonJ,buttonK,buttonL)
    markup2.row(buttonZ,buttonX,buttonC,buttonV,buttonB,buttonN,buttonM,)
    bot.send_message(message.chat.id, 'working',reply_markup=markup2, )

@bot.message_handler(content_types='text')
def say_any(message):
    audio_name = datetime.datetime.now()
    text = message.text
    say = gtts.gTTS(text, lang='ru', slow=False)
    say.save(f'{audio_name}.mp3')
    final_path = f'{current_path}/{audio_name}.mp3'
    audio_file = open(final_path, 'rb')
    bot.send_audio(message.chat.id, audio_file)
    # bot.send_message(message.chat.id, "I have sended!")

from time import sleep
from rich.console import Console

console = Console()
tasks = [f"task {n}" for n in range(1, 11)]

with console.status("[bold red]Working on tasks...") as status:
    while tasks:
        task = tasks.pop(0)
        sleep(1)
        console.log(f"\r{task} complete")

print ('Bot is working!')
bot.infinity_polling()