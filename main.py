import telebot
from telebot.util import quick_markup
from dotenv.main import load_dotenv
import os
from twt import twitter_dl_video
from tktk import tiktok_dl_video
from ig import ig_dl_video
from igPics import ig_pfp

load_dotenv()
API_KEY = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(API_KEY)

# decorator


# returns an InlineKeyboardMarkup with two buttons in a row, one leading to Twitter, the other to facebook
# and a back button below

# kwargs can be:
{
    'url': None,
    'callback_data': None,
    'switch_inline_query': None,
    'switch_inline_query_current_chat': None,
    'callback_game': None,
    'pay': None,
    'login_url': None,
    'web_app': None
}


@bot.message_handler(commands=['start'])
def response(message):
    # print(message)
    bot.reply_to(message, "Hello, I'm a bot")


@bot.message_handler(commands=['mensagem'])
def response(message):
    # print(message)
    text = """
    oi bobão, eu sou um bot (eu sei seu endereço)
    """
    bot.reply_to(message, text)


def itboy(message):
    if message.text == "Quem é o it boy da quarta geração?":
        return True
    else:
        return False


@bot.message_handler(func=itboy)
def response(mensagem):
    print(mensagem)
    text = """O it boy da quarta geração é Choi Yeonjun, do grupo TXT"""
    bot.reply_to(mensagem, text)


def verifyTwitterLink(message):
    if message.text[0:19] == "https://twitter.com":
        return True
    elif message.text[0:23] == "https://mobile.twitter.com":
        return True
    elif message.text[0:13] == "https://x.com":
        return True
    else:
        return False


@bot.message_handler(func=verifyTwitterLink)
def response(mensagem):
    print(mensagem)
    path_arr = twitter_dl_video(mensagem.text)
    text = """
    legao esse link do twitter hein"""
    bot.reply_to(mensagem, text)
    print(path_arr)
    bot.send_video(mensagem.chat.id, open(path_arr[0], 'rb'))
    bot.send_audio(mensagem.chat.id, open(path_arr[1], 'rb'))


def verifyTiktokLink(message):
    if message.text[0:22] == "https://www.tiktok.com":
        return True
    else:
        return False


@bot.message_handler(func=verifyTiktokLink)
def response(mensagem):
    print(mensagem)
    path_arr = ig_pfp(mensagem.text)
    text = """
    legau esse link do Tiktok hein"""
    bot.reply_to(mensagem, text)
    bot.send_video(mensagem.chat.id, open(path_arr[0], 'rb'))
    bot.send_audio(mensagem.chat.id, open(path_arr[1], 'rb'))


def verifyInstagramLink(message):
    if message.text[0:25] == "https://www.instagram.com":
        return True
    else:
        return False


captions = {}  # Dicionário para armazenar legendas


@bot.message_handler(func=verifyInstagramLink)
def response(mensagem):
    mediaArr, caption, criadoEm, mediaCount = ig_pfp(
        mensagem.text, "ab6ix_official")
    noImg = """Hmm... parece que não tem imagens nesse post"""
    noCaption = """Hmm... parece que não tem legenda nesse post"""

    # bot.reply_to(mensagem, text)
    print(mediaArr)

    if mediaCount == 1:
        bot.send_photo(mensagem.chat.id, open(
            mediaArr[0], 'rb'), caption=caption)
    elif mediaCount == 0:
        bot.reply_to(mensagem, noImg)
    else:
        for media in mediaArr[0:]:
            bot.send_document(mensagem.chat.id, open(media, 'rb'))
            
    if caption == None:
        bot.reply_to(mensagem, noCaption)
    else:
        bot.reply_to(mensagem, """Legenda pra traduzir:""")
        bot.send_message(mensagem.chat.id, caption)

    


# MENSAGEM PADRAO
def verify(message):
    return True


@bot.message_handler(func=verify)
def response(mensagem):
    print(mensagem)

    text = """
    Escolha uma das opções abaixo:
/start - Iniciar
/mensagem - Ver uma mensagem fofa
Não tem outros comandos"""
    bot.reply_to(mensagem, text)


bot.polling()
