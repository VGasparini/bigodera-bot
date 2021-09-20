import os, time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Chat
from requests import post, get, delete
import logging
import random as r
import time
from math import sqrt, gcd, log
from itertools import count, islice

api_location = 'https://api-bigodera.herokuapp.com/'

# function to handle the /start command
def start(update, context):
    chat_id = update.message.chat_id
    text = "Bigodera acordado! Agora você já pode utilizar alguns de meus comando. Veja uma lista dos comandos digitando /help"
    update.message.reply_text(text)

# function to handle the /help command
def help(update, context):
    text = (
        "Tenho as seguintes funcionalidades\n"
        + "/start - Me acorda caso esteja dormindo\n"
        + "/on - Verifica se eu estou acordado\n"
        + "/meme - Frases icônicas de pessoas mais ainda\n"
        + "/add_meme meme - Adicionar um meme\n"
        + "/linkar_cf handle - Liga o handle à sua conta do Telegram\n"
        + "/deslinkar_cf - Desvincula seu handle do codeforces da sua conta do Telegram\n"
        + "/probleminha rating [tags] - Escolhe um problema aleatório do codeforces para seu handle cadastrado\n"
        + "/roll n t - Rola n dados de t faces\n"
        + "/even_odd - O famoso par ou impar\n"
        + "/primo n - Verifica se n é primo\n"
        + "/calculadora a op b - Faz o calculo, +,-,*,**,%,^ ex: 1 + 1\n"
        + "/contador_caga_pau - É tanta cagada de pau que nem dá pra contar\n"
        + "/incrementa_contador_caga_pau - Alguém cagou no pau '-'\n"
        + "/fatorar n1 [n2 n3 ... n10] - Realiza a fatoração (máximo de 10 números por comando)"
        # + "/mute - Apenas admins, muta o Machado\n"
        # + "/unmute - Deixa o garoto falar merda vai..."
    )
    update.message.reply_text(text)

def on(update, context):
    update.message.reply_text("To de pé rs")

def greet(update, context):
    global api_location
    for new_user_obj in update.message.new_chat_members:
        text = get(api_location+'greet/'+new_user_obj.split()[0]).json()['1']
        update.message.reply_text(text)

def noncommand(update, context):
    text = (update.message.text).lower()
    ret = ""
    if "caga pau" in text:
        ret = "FELIPE WEISS"
    elif "felipe weiss" in text:
        ret = "caga pau"
    elif "sei la" in text:
        ret = "treze"
    elif "porra" in text and "caralho" in text:
        ret = "Ambiente Familiar"
    elif "bigod" in text and text[-1] == "?":
        ret = "sim"
    elif "gasp" in text and text[-1] == ".":
        ret = "cara é bom!"
    elif "cara" == text.split()[0]:
        carinhas = ["'-'", "'.'", "XD", "u.u", "@.@", ".-.", ":c"]
        ret = r.choice(carinhas)
    elif "bom dia" in text and text[-1] == "!":
        ret = "O sol nasceu na puta que pariu do horizonte, para iluminar a porra dos seus sonhos, bom dia filha da putaaa"
    elif "boa noite" in text:
        ret = "Já vai tarde..."
    elif "melhor da vida" in text:
        quotes = [
            "pao de alho",
            "acordar cedo e lembrar que é sábado",
            "mijar apertado",
            "borda recheada de brinde",
            "quando chega o que vc comprou pela internet",
            "frete grátis",
            "achar dinheiro no bolso",
            "wifi grátis",
            "final da nacional",
        ]
        ret = r.choice(quotes)

    if ret:
        update.message.reply_text(ret)

def meme(update, context):
    global api_location
    api_data = get(api_location+'meme')
    text = api_data.json()['1']
    update.message.reply_text(text)

def add_meme(update, context):
    global api_location
    new_meme = ' '.join(update.message.text.split(' ')[1:])
    text = post(api_location+'add_meme', json={'new_meme': new_meme}).json()['1']
    update.message.reply_text(text)

def birthday(update, context):
    global api_location
    name = update.message.text.split()[1]
    text = get(api_location+'birthday/'+name).json()['1']
    update.message.reply_text(text)
# function to handle errors occured in the dispatcher

def user(update, context):
    global api_location
    user_id = update.message.from_user.id
    handle = ' '.join(update.message.text.split(' ')[1:])
    text = post(api_location+'user', json = {'handle': handle, 'id_telegram': int(user_id)}).json()['1']
    update.message.reply_text(text)

def del_user(update, context):
    global api_location
    user_id = update.message.from_user.id
    text = delete(api_location+'del_user', json = {'id_telegram': int(user_id)}).json()['1']
    update.message.reply_text(text)

def cf_problem(update, context):
    global api_location
    user_id = update.message.from_user.id
    split_message = update.message.text.split(' ')
    if (len(split_message) == 1):
        text = post(api_location+'cfproblem', json={'id_telegram': int(user_id)}).json()['1']
        update.message.reply_text(text)
    else:
        rating = split_message[1]
        tags = ''
        if (len(split_message) > 2):
            tags = ' '.join(split_message[2:])
        text = post(api_location+'cfproblem', json={'id_telegram': int(user_id), 'rating': int(rating), 'tags': tags}).json()['1']
        update.message.reply_text(text)

def contador_caga_pau(update, context):
    global api_location
    text = get(api_location+'contador_caga_pau').json()['1']
    update.message.reply_text(text)

def inc_contador_caga_pau(update, context):
    global api_location
    text = get(api_location+'contador_caga_pau++').json()['1']
    update.message.reply_text(text)

def roll(update, context):
    global api_location
    args = update.message.text.split(' ')[1:]
    dados = args[0]
    lados = args[1]
    results = post(api_location+'roll', json={'dados': dados, 'lados': lados}).json()
    text = ''
    if (results == {'1' : 'Vsf! Porrada de Dado.'}):
        update.message.reply_text('Vsf! Porrada de Dado.')
        return
    for dado in results:
        text += str(dado) + ': ' + str(results[dado]) + '\n'
    update.message.reply_text(text[:len(text)-1])

def even_odd(update, context):
    global api_location
    text = get(api_location+'even_odd').json()['1']
    update.message.reply_text(text)

def primo(update, context):
    global api_location
    numbers = ' '.join(update.message.text.split(' ')[1:])
    results = post(api_location+'primo', json={'numbers': numbers}).json()
    text = ''
    for line in results:
        text += results[line]+'\n'
    update.message.reply_text(text[:len(text)-1])

def fatorar(update, context):
    global api_location
    numbers = ' '.join(update.message.text.split(' ')[1:])
    # print(numbers)
    results = post(api_location+'fatorar', json={'numbers': numbers}).json()
    text = ''
    for number in results:
        text += str(number) + ': ' + results[number] + '\n'
    update.message.reply_text(text[:len(text)-1])

def calculadora(update, context):
    global api_location
    split_message = update.message.text.split(' ')
    # print(split_message)
    try:
        number1 = split_message[1]
        operation = split_message[2]
        number2 = split_message[3]
        text = post(api_location+'calculadora', json={'number1': float(number1), 'number2': float(number2), 'operation': operation}).json()['1']
        update.message.reply_text(text)
    except:
        update.message.reply_text('Um erro ocorreu')

def error(update, context):
    update.message.reply_text('Update "%s" caused error "%s"', update, error)


# function to handle normal text
# def text(update, context):
#     text_received = update.message.text
#     update.message.reply_text(f'did you said "{text_received}" ?')



def main():
    # tfile = open('bot_token', 'r')
    TOKEN = os.environ["TELEGRAM_TOKEN"]

    # create the updater, that will automatically create also a dispatcher and a queue to
    # make them dialoge
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # add handlers for start and help commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("meme", meme))
    dispatcher.add_handler(CommandHandler("add_meme", add_meme))
    dispatcher.add_handler(CommandHandler("on", on))
    dispatcher.add_handler(CommandHandler("greet", greet))
    dispatcher.add_handler(CommandHandler("feliz_aniversario",birthday))
    dispatcher.add_handler(CommandHandler("linkar_cf",user))
    dispatcher.add_handler(CommandHandler("deslinkar_cf",del_user))
    dispatcher.add_handler(CommandHandler("probleminha",cf_problem))
    dispatcher.add_handler(CommandHandler("contador_caga_pau",contador_caga_pau))
    dispatcher.add_handler(CommandHandler("incrementa_contador_caga_pau",inc_contador_caga_pau))
    dispatcher.add_handler(CommandHandler("roll",roll))
    dispatcher.add_handler(CommandHandler("even_odd",even_odd))
    dispatcher.add_handler(CommandHandler("primo",primo))
    dispatcher.add_handler(CommandHandler("fatorar",fatorar))
    dispatcher.add_handler(CommandHandler("calculadora",calculadora))

    # dispatcher.add_handler(MessageHandler(Filters.text, text))

    # add an handler for normal text (not commands)
    dispatcher.add_handler(MessageHandler(Filters.text, noncommand))

    # add an handler for errors
    dispatcher.add_error_handler(error)

    # start your shiny new bot
    updater.start_polling()

    # run the bot until Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
