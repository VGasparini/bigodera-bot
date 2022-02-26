from random import choice

def noncommand(update, context):
    chat_text = (update.message.text).lower()
    reply_text = ""
    if "caga pau" in chat_text:
        reply_text = "FELIPE WEISS"
    elif "felipe weiss" in chat_text:
        reply_text = "caga pau"
    elif "sei la" in chat_text:
        reply_text = "treze"
    elif "porra" in chat_text and "caralho" in chat_text:
        reply_text = "Ambiente Familiar"
    elif "bigod" in chat_text and chat_text[-1] == "?":
        reply_text = "sim"
    elif "gasp" in chat_text and chat_text[-1] == ".":
        reply_text = "cara é bom!"
    elif "cara" == chat_text.split()[0]:
        carinhas = ["'-'", "'.'", "XD", "u.u", "@.@", ".-.", ":c"]
        reply_text = choice(carinhas)
    elif "bom dia" in chat_text and chat_text[-1] == "!":
        reply_text = "O sol nasceu na puta que pariu do horizonte, para iluminar a porra dos seus sonhos, bom dia filha da putaaa"
    elif "boa noite" in chat_text:
        reply_text = "Já vai tarde..."
    elif "melhor da vida" in chat_text:
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
        reply_text = choice(quotes)

    if reply_text:
        update.message.reply_text(reply_text)
