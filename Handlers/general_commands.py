from misc import bot


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, "Hi! Please send me any geolocation and I'll record this place")


@bot.message_handler(commands=['help'])
def help_handler(message):
    bot.send_message(message.chat.id, "Please send me any geolocation and I'll record this place")
