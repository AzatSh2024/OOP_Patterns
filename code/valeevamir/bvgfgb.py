import telebot
@bot.message (commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message,"Привет, рад тебя видеть ")

@bot.message (func=lambda message: True)
def echo_all(message):
    if message.text == "привет":
        bot.reply_to(message, "Привет, мой друг")
    elif message.text == "как дела?":
        bot.reply_to(message, "Все хорошо, как твои дела?")
        if message.text == "как дела":
            bot.reply_to(message, "Отлично, как твои дела?")

        # bot.reply_to(message, message.text)

    bot.infinity_polling()
