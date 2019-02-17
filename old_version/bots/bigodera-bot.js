var TelegramBot = require('node-telegram-bot-api');
var token = require('../token.json');
var fs = require('fs');
var bot = new TelegramBot(token.token, {polling: true});

bot.onText(/.*melhor .*vida/i,function(msg) {
    var chatId = msg.chat.id;
    var n = Math.random() * 9;
    var ret;
    if(n < 1) ret = 'pao de alho';
    else if (n < 2) ret = 'acordar cedo e lembrar que é sábado';
    else if (n < 3) ret = 'mijar apertado';
    else if (n < 4) ret = 'borda recheada de brinde';
    else if (n < 5) ret = 'quando chega o que vc comprou pela internet';
    else if (n < 6) ret = 'frete grátis';
    else if (n < 7) ret = 'achar dinheiro no bolso';
    else if (n < 8) ret = 'wifi grátis';
    else ret = 'final da nacional';
    bot.sendMessage(chatId, ret);
});

bot.onText(/(caga pau)/i,function(msg){
    var chatId = msg.chat.id;
    bot.sendMessage(chatId, 'FELIPE WEISS');
});

bot.onText(/(felipe weiss)/i,function (msg) {
    var chatId = msg.chat.id;
    bot.sendMessage(chatId, 'CAGA PAU');
});

bot.onText(/pt/i,function(msg) {
    var chatId = msg.chat.id;
    bot.sendMessage(chatId, 'TREZE');
});

bot.onText(/porra/i,function(msg) {
    var chatId = msg.chat.id;
    bot.sendMessage(chatId, 'Ambiente Familiar');
});

bot.onText(/^(bigod).*[?]$/i,function(msg) {
    var chatId = msg.chat.id;
    bot.sendMessage(chatId, 'sim');
});

bot.onText(/.*gasp \.$/i,function(msg) {
    var chatId = msg.chat.id;
    bot.sendMessage(chatId, 'O cara é bom!');
});

bot.onText(/bolso/i,function(msg) {
    var chatId = msg.chat.id;
    bot.sendMessage(chatId, 'Tem que acabar isso dai ta ok');
});

bot.onText(/('\.'|'-'|XD|u\.u|@\.@|\.-\.|:c)/i, function (msg) {
    var chatId = msg.chat.id;
    bot.sendMessage(chatId, 'lixo');
});

bot.onText(/(boa noite)/i, function (msg) {
    var chatId = msg.chat.id;
    bot.sendMessage(chatId, 'Boa noite! Durma bem');
});

bot.onText(/(bom dia)/i, function (msg) {
    var chatId = msg.chat.id;
    bot.sendMessage(chatId, 'Bom dia! Bora ser hoje menos arrombado que ontem');
});

bot.onText(/\/start/,function(msg) {
    var chatId = msg.chat.id;
    bot.sendMessage(chatId, 'Bigodera acordado! Agora você já pode utilizar alguns de meus comando. Tente por /help');
});

bot.onText(/\/help/,function(msg) {
	var chatId = msg.chat.id;
    bot.sendMessage(chatId, 'Tenho as seguintes funcionalidade\n /start - Me acorda caso esteja dormindo\n /greet - Saudação\n /meme - Frases icônicas de pessoas mais ainda\n');
});

bot.onText(/\/greet/,function(msg){
    var pre = Array('e ai ', 'opa ', 'olá ', 'oie ', 'turu bom ');
    var suf = Array('pro URI', 'pro RU', 'pro codeforces', 'pro code', 'pra maratona');
    var greeting = pre[Math.floor(Math.random() * pre.length)];
    var chatId = msg.chat.id;
    var who = msg.from.first_name;
    bot.sendMessage(chatId, ''.concat(greeting.capitalize(),who,', bem vindo ao BRUTE. Eu sou o Bigodera, o bot dessa galera. Bora ',suf[Math.floor(Math.random()*suf.length)] ));
});
            
bot.onText(/\/meme/,function(msg) {
    var quotes = Array('Weiss caga pau','socável', 'campeão sul brasileiro', 'o balão mais rapido do brasil', 'o cara que anima o time', 'carregou mais que Noé', 'cade meu vinho', 'Jonck me deve 25 pila');
    var chatId = msg.chat.id;
    bot.sendMessage(chatId, quotes[Math.floor(Math.random()*quotes.length)]);
});

bot.onText(/luz/i, function (msg) {
    var chatId = msg.chat.id;
    bot.sendMessage(chatId, 'vao tudo tomar no cu');
});

module.exports = bot;

// JS stuff

String.prototype.capitalize = function () {
    return this.charAt(0).toUpperCase() + this.slice(1);
}

