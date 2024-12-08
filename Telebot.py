import telebot
TOKEN = '8064497911:AAFzALVPTLQbBAY0XWZe0GvuqLUugA995DY'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(message.chat.id, 'Привет! ' + message.from_user.first_name)
  bot.send_message(message.chat.id, message.text)

bot.polling()



from g4f.client import Client
import telebot
TOKEN = '8064497911:AAFzALVPTLQbBAY0XWZe0GvuqLUugA995DY'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(message.chat.id, 'Привет! ' + message.from_user.first_name)

@bot.message_handler(content_types=['text'])
def text(message):
  client = Client()
  response = client.chat.completions.create(
      model="gpt-4o",
      messages=[{"role": "user", "content": message.text}],
  )
  bot.send_message(message.chat.id, response.choices[0].message.content)

bot.polling()




