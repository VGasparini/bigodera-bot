require 'telegram_bot'

token = ''

bot = TelegramBot.new(token: token)

bot.get_updates(fail_silently: true) do |message|
	puts "@#{message.from.first_name}: #{message.text}"
	command = message.get_command_for(bot)
	message.reply do |reply|		
		if command == '/start'
			reply.text = "Bigodera acordado! Agora você já pode utilizar alguns de meus comando. Tente por /help"
		elsif (command =~ /\d/)+1
			reply.text = "Coisa de comunista isso ai, ta ok" 
		elsif command == '/help/i'
			reply.text = "Tenho as seguintes funcionalidade\n /start - Me acorda caso esteja dormindo\n /greet - Recepção\n /Weiss - Apenas a verdade"
		elsif command == '/greet/i'
			saudacao = ['e ai', 'opa', 'olá', 'oie', 'turu bom']
			final = ['pro URI', 'pro RU', 'pro codeforces', 'pro code', 'pra maratona']
			reply.text = "#{saudacao.sample.capitalize} #{message.from.first_name}, bem vindo ao BRUTE. Eu sou o Bigodera, o bot dessa galera. Bora #{final.sample}!"
		elsif command == '/weiss/i'
			wes = ['o caga pau', 'vermelho', 'socável', 'campeão sul brasileiro']
			reply.text = "#{wes.sample.capitalize}"
		elsif command == '/jonck/i'
			jnk = ['o engraçado', 'humilde', 'o cara que anima o time', 'campeão sul brasileiro']
			reply.text = "#{jnk.sample.capitalize}"
		elsif command == '/felipera/i'
			felipe = ['o rápido', 'carregou mais que Noé', 'cadê meu vinho?', 'campeão sul brasileiro']
			reply.text = "#{felipe.sample.capitalize}"
		else
			reply.text = "Eu não faço ideia do que significa #{command.inspect}.\nFala com o Gasparini se acha que aconteceu algum erro ou uma função massa de ter."
		end
		puts "sending #{reply.text.inspect} to @#{message.from.first_name}"
		reply.send_with(bot)
	end
end