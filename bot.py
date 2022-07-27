
import sqlite3
from textwrap import indent
import telebot
from telebot import types
bot = telebot.TeleBot("5430333457:AAGYE_-8rPStk8rfwIXGrfC7pQqDkzOtql0")





@bot.message_handler(commands='help')
def send_welcome(message):
	bot.send_message(message.chat.id, "Напиши /start")

@bot.message_handler(commands='start')
def send_welcome(message):
	bot.send_message(message.chat.id, "Привет, из какого ты города?")
	bot.register_next_step_handler(message, reg_name)


def reg_name(message):
	city = message.text
	user_id = message.from_user.id 
	con = sqlite3.connect("weatherusers.db")
	cur  = con.cursor()
	conn = sqlite3.connect('cities.db')
	curr  = conn.cursor()
	curr.execute('''select * from cities where Город =  :city''', {'city':city})

	city_id = curr.fetchone()[0]
	if city_id == None:
		bot.send_message(message.chat.id, 'Такого города нет(')
	else:
		cur.execute('insert into weatherusers values (?,?)', (user_id, city_id))

	con.commit()
	con.close()



bot.polling(none_stop=True)

