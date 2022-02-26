from requests import post, get, delete

API_ADDRS = os.environ["API_ADDRESS"]


def help(update, context):
    text = """Tenho as seguintes funcionalidades\n
        /bot_status - Verifica se eu estou acordado\n
        /meme - Frases icônicas de pessoas mais ainda\n
        /add_meme meme - Adicionar um meme\n
        /contador_caga_pau - É tanta cagada de pau que nem dá pra contar\n
        /mais_uma_cagada - Alguém cagou no pau '-'\n
        /linkar_cf handle - Liga o handle à sua conta do Telegram\n
        /deslinkar_cf - Desvincula seu handle do codeforces da sua conta do Telegram\n
        /probleminha rating [tags] - Escolhe um problema aleatório do codeforces para seu handle cadastrado\n
        /roll n t - Rola n dados de t faces\n
        /even_odd - O famoso par ou impar\n
        /primo n - Verifica se n é primo\n
        /calcular a op b - Faz o calculo com seguintes operadores +,-,*,**,%,^ ex: 1 + 1\n
        /fatorar n1 [n2 n3 ... n10] - Realiza a fatoração (máximo de 10 números por comando)"""
    update.message.reply_text(text)


def bot_status(update, context):
    response = get(API_ADDRS)

    api_status = "🟢"
    if response.status_code != 200:
        api_status += "🔴"
    update.message.reply_text(f"Bot status: 🟢\nAPI status: {api_status}")


def meme(update, context):
    response = get(f"{API_ADDRS}/meme")

    text = response.json()["data"]
    update.message.reply_text(text)


def add_meme(update, context):
    new_meme = " ".join(update.message.text.split(" ")[1:])
    response = post(f"{API_ADDRS}/add_meme", json={"new_meme": new_meme})

    text = response.json()["data"]
    update.message.reply_text(text)


def contador_caga_pau(update, context):
    response = get(f"{API_ADDRS}/contador_caga_pau")

    text = response.json()["data"]
    update.message.reply_text(text)


def mais_uma_cagada(update, context):
    response = post(f"{API_ADDRS}/mais_uma_cagada", json={"amount": 1})

    text = response.json()["data"]
    update.message.reply_text(text)


def linkar_cf(update, context):
    user_id = update.message.from_user.id
    handle = " ".join(update.message.text.split(" ")[1:])
    response = post(
        f"{API_ADDRS}/user", json={"handle": handle, "id_telegram": int(user_id)}
    )

    text = response.json()["data"]
    update.message.reply_text(text)


def deslinkar_cf(update, context):
    user_id = update.message.from_user.id
    response = delete(f"{API_ADDRS}/del_user", json={"id_telegram": int(user_id)})

    text = response.json()["data"]
    update.message.reply_text(text)


def probleminha(update, context):
    args = update.message.text.split(" ")
    user_id = update.message.from_user.id
    rating = None
    tags = None

    if len(args) > 1:
        rating = args[1]
        if len(args) > 2:
            tags = " ".join(args[2:])

    request_payload = {"id_telegram": user_id, "rating": rating, "tags": tags}
    response = post(
        f"{API_ADDRS}/cfproblem",
        json=request_payload,
    )

    text = response.json()["data"]
    update.message.reply_text(text)


def roll(update, context):
    args = update.message.text.split(" ")[1:]
    dice_amount = args[0]
    dice_size = args[1]
    response = post(
        f"{API_ADDRS}/roll", json={"dados": dice_amount, "lados": dice_size}
    )

    if response.status_code == 403:
        text = response.json()["data"]
        update.message.reply_text(text)
        return

    results = response.json()["dices"]
    text = ""
    for dice_result in results:
        idx, value = next(iter(dice_result.items()))
        text += f"{idx} : {value}\n"
    update.message.reply_text(text)


def even_odd(update, context):
    response = get(f"{API_ADDRS}/even_odd")

    text = response.json()["data"]
    update.message.reply_text(text)


def primo(update, context):
    numbers = " ".join(update.message.text.split(" ")[1:])
    response = post(f"{API_ADDRS}/primo", json={"numbers": numbers})

    results = response.json()["data"]
    text = ""
    for line in results:
        text += f"{results[line]}\n"
    update.message.reply_text(text)


def calcular(update, context):
    args = update.message.text.split(" ")
    number1 = args[1]
    operation = args[2]
    number2 = args[3]
    response = post(
        f"{API_ADDRS}/calculadora",
        json={
            "number1": float(number1),
            "number2": float(number2),
            "operation": operation,
        },
    )

    if response.status_code == 403:
        text = response.json()["msg"]
        update.message.reply_text(text)
        return

    text = response.json()["data"]
    update.message.reply_text(text)


def fatorar(update, context):
    numbers = " ".join(update.message.text.split(" ")[1:])
    response = post(f"{API_ADDRS}/fatorar", json={"numbers": numbers})

    results = response.json()
    text = ""
    for number in results:
        text += f"{number} : {results[number]}\n"
    update.message.reply_text(text)
