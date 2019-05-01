# -*- coding: utf-8 -*-
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Job
import logging
import json
import random as r

# token = os.environ['TELEGRAM_TOKEN']
token = '753464946:AAEn_H8nVJBaNAY3rDAtrQSdftOE4NOepdU'
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
updater = Updater(token)

# Functions noncommand
def noncommand(bot, update):
    text = (update.message.text).lower()
    ret = ''
    if 'caga pau' in text:
        ret = caga_pau()
    elif 'felipe weiss' in text:
        ret = felipe_weiss()
    elif 'pt' in text:
        ret = pt()
    elif 'porra' in text:
        ret = familiar()
    elif 'bigod' in text and text[-1] == '?':
        ret = bigodera_pergunta()
    elif 'gasp' in text and text[-1] == '.':
        ret = cara_bom()
    elif 'cara' == text.split()[0]:
        ret = carinhas()
    elif 'bom dia' in text:
        ret = bom_dia()
    elif 'boa noite' in text:
        ret = boa_noite()
    elif 'melhor da vida' in text:
        ret = melhor_vida()
      
    if ret: update.message.reply_text(ret)

def melhor_vida():
    quotes = ['pao de alho', 'acordar cedo e lembrar que é sábado', 'mijar apertado',
            'borda recheada de brinde', 'quando chega o que vc comprou pela internet',
            'frete grátis', 'achar dinheiro no bolso', 'wifi grátis', 'final da nacional']
    return quotes[r.randrange(len(quotes))]

def caga_pau():
    return 'FELIPE WEISS'

def felipe_weiss():
    return 'CAGA PAU'

def pt():
    return 'TREZE'

def familiar():
    return 'Ambiente Familiar'

def bigodera_pergunta():
    return 'sim'

def cara_bom():
    return 'O cara é bom!'

def carinhas():
    quotes = ["'-'","'.'","XD","u.u","@.@",".-.",":c"]
    return quotes[r.randrange(len(quotes))]

def boa_noite():
    return 'Boa noite! Durma bem'

def bom_dia():
    return 'Bom dia! Bora ser hoje menos arrombado que ontem'


#Functions commanded
def start(bot, update):
    chat_id = update.message.chat_id
    text = 'Bigodera acordado! Agora você já pode utilizar alguns de meus comando. Tente por /help'
    bot.sendMessage(chat_id = chat_id, text = text)

def help(bot, update):
    chat_id = update.message.chat_id
    text = ('Tenho as seguintes funcionalidade\n'+
            '/start - Me acorda caso esteja dormindo\n'+
            '/greet - Saudação\n'+
            '/meme - Frases icônicas de pessoas mais ainda\n'+
            '/roll n - Rola um dado n ')
    bot.sendMessage(chat_id = chat_id, text = text)

def greet(bot, update):
    pre = ['E ai ', 'Opa ', 'Olá ', 'Oie ', 'Turu bom ']
    suf = ['pro URI', 'pro RU', 'pro codeforces', 'pro code', 'pra maratona']
    g1 = pre[r.randrange(len(pre))]
    g2 = suf[r.randrange(len(pre))]
    chat_id = update.message.chat_id
    who = update.message.from_user.first_name
    text = g1 + who.capitalize() + ', bem vindo ao BRUTE. Eu o Bigodera, o bot desssa galera. Bora ' + g2
    bot.send_message(chat_id = chat_id, text = text)

def meme(bot, update):
    quotes = ['Weiss caga pau', 'socável', 'campeão sul brasileiro',
    'o balão mais rapido do brasil', 'o cara que anima o time',
    'carregou mais que Noé', 'cade meu vinho', 'Jonck me deve 25 pila',
    'sou o mais parceiro', 'Adilsoney' , 'Poderia ser pior... Podia ser Adilson',
    'só trocar o if por um for', 'dieta Cattonica', 'três passos a frente',
    'qué vê?', 'se der bizu…', 'confia no rand()', 'uma salva de palmas...',
    'gadão']
    chat_id = update.message.chat_id
    text = quotes[r.randrange(len(quotes))]
    bot.send_message(chat_id = chat_id, text = text)

def roll(bot, update):
    text = update.message.text.split()[1:]
    times,limit = map(int,text)
    text = "Rolando!\n\n"
    for dice in range(1,times+1):
        text += str(r.randint(1,limit))+"\n"
    chat_id = update.message.chat_id
    bot.send_message(chat_id = chat_id, text = text)


# def divida(bot, update):
#     text = update.message.text  
#     if 'deve' in text: # /divida jonck me deve 15
#         me = update.message.from_user.username
#         t = text.split()
#         to = t[1]
#         val = t[-1]
#         add_div(me,to+' '+val)
#     if 'paguei' in text: # /divida paguei 15 ao jonck
#         me = update.message.from_user.username
#         t = text.split()
#         to = t[-1]
#         val = t[2]
#         add_div(me,to+' '+val)
#     if 'minhas dividas' in text:
#         me = update.message.from_user.username
#         update.message.reply_text(show_div(me))
#     if 'help' in text:
#         bot.send_message(chat_id = update.message.chat_id,
#                                     text = '/divida (quem te deve) me deve (valor)\n'+
#                                             '/divida paguei (valor) (quem tu pagou)\n\n'+
#                                             'Padrão dos nomes\n'+
#                                             'Gasparini\nWeiss\nCarol\nJonck\nLuiza')

def error(bot, update, error):
        logger.warning('Update "%s" caused error "%s"', update, error)

def main():
        """Start the bot."""
        # Get the dispatcher to register handlers
        dp = updater.dispatcher

        # Answer in Telegram
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))
        dp.add_handler(CommandHandler("greet", greet))
        dp.add_handler(CommandHandler("meme", meme))
        dp.add_handler(CommandHandler("roll", roll))
        # dp.add_handler(CommandHandler("divida", divida))

        # Noncommand answser message on Telegram
        dp.add_handler(MessageHandler(Filters.text, noncommand))

        # log all errors
        dp.add_error_handler(error)

        # Start the Bot
        updater.start_polling()

        # start_polling() is non-blocking and will stop the bot gracefully.
        updater.idle()


if __name__ == '__main__':
        main()  
