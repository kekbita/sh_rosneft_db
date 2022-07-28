
import sqlite3
from textwrap import indent
import telebot
from telebot import types
bot = telebot.TeleBot("5430333457:AAGYE_-8rPStk8rfwIXGrfC7pQqDkzOtql0")


def reg_name(message):
	city = message.text
	user_id = message.from_user.id 
	con = sqlite3.connect("weatherusers.db")
	cur  = con.cursor()
	conn = sqlite3.connect('cities.db')
	curr  = conn.cursor()
	curr.execute('''select * from cities where Город =  :city''', {'city':city})
	
	city_from_db = curr.fetchone()
	if city_from_db == None:
		bot.send_message(message.chat.id, 'Такого города нет(')
	else:
		cur.execute('insert into weatherusers values (?,?)', (user_id, city_from_db[0]))

	con.commit()
	con.close()


def get_user_lat_lon(user_id):
	con = sqlite3.connect("weatherusers.db")
	cur  = con.cursor()
	conn = sqlite3.connect('cities.db')
	curr  = conn.cursor()
	cur.execute('''select * from weatherusers where user_id = :user_id''', {'user_id': user_id})
	city_id = cur.fetchone()[1]
	curr.execute('''select * from cities where city_id = :city_id''', {'city_id':city_id})
	lat_lon= curr.fetchone()
	lat = lat_lon[2]
	lon = lat_lon[3]
	return lat, lon

def get_all_users():
	con = sqlite3.connect('weatherusers.db')
	cur = con.cursor()
	cur.execute('''select user_id from weatherusers''')

	user_ids = cur.fetchall()
	return list(x[0] for x in user_ids)
print(get_all_users())
bot.polling(none_stop=True)

