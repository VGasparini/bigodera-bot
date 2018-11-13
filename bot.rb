require 'telegram_bot'

token = 

bot = TelegramBot.new(token: token)

bot.get_updates(fail_silently: true) do |message|
	puts "@#{message.from.username}: #{message.text}"
	command = message.get_command_for(bot)

	message.reply do |reply|
		case command
		when /start/i
			reply.text = "Bigodera acordado! Agora você já pode utilizar alguns de meus comando. Tente por /help"

		when /help/i
			reply.text = "Tenho as seguintes funcionalidade\n /start - Me acorda caso esteja dormindo\n /greet - Recepção\n /Weiss - Apenas a verdade"

		when /greet/i
			saudacao = ['e ai', 'opa', 'olá', 'oie', 'turu bom']
			final = ['pro URI', 'pro RU', 'pro codeforces', 'pro code', 'pra maratona']
			reply.text = "#{saudacao.sample.capitalize} #{message.from.first_name}, bem vindo ao BRUTE. Eu sou o Bigodera, o bot dessa galera. Bora #{final.sample}!"

		when /weiss/i
			wes = ['o caga pau', 'vermelho', 'socável']
			reply.text = "#{wes.sample.capitalize}"

		when /jonck/i
			jnk = ['o engraçado', 'humilde', 'o cara que anima o time']
			reply.text = "#{jnk.sample.capitalize}"

		when /felipera/i
			felipe = ['o hacker', 'carregou mais que Noé', 'cadê meu vinho?']
			reply.text = "#{felipe.sample.capitalize}"
		
		else
			reply.text = "Eu não faço ideia do que significa #{command.inspect}.\nFala com o Gasparini se acha que aconteceu algum erro ou uma função massa de ter."
		
		end
		puts "sending #{reply.text.inspect} to @#{message.from.username}"
		reply.send_with(bot)
	end
end