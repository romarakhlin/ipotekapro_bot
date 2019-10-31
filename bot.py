import telebot
from telebot import types
import smtplib
import os
import mimetypes
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

token = '974041945:AAHPwebQF4DP8Z4ulqq8m1vf-YIoa1AnKNg'
bot = telebot.TeleBot(token)

answers = []
sost = 0
n = 0
m = 0

def sending(id, message):
	global my_list, n, sost, answers
	if n == 4:
		bot.send_message(id,'Спасибо за обращение! Ближайщее время мы свяжемся с Вами')
		answers.append('город: ' + message.text)
		s = ''
		for i in range(len(answers)):
			s += str(answers[i]) + '\n'
		def send_email(addr_from, password, addr_to):
		    msg_subj = 'Новая анкета'
		    msg_text = s
		    msg = MIMEMultipart()
		    msg['From'] = addr_from
		    msg['To'] = addr_to
		    msg['Subject'] = msg_subj
		    body = msg_text
		    msg.attach(MIMEText(body, 'plain'))
		    server = smtplib.SMTP('smtp.yandex.ru', 587)
		    server.starttls()
		    server.login(addr_from, password)
		    server.send_message(msg)
		    server.quit()
		_from = 'rrakhlin23@yandex.ru'
		_password = 'Vladik0404'
		_to = 'contrust24@gmail.com'
		send_email(_from, _password, _to)
		sost = 0
	elif n == 1:
		bot.send_message(id, 'Ваш телефон: ')
		answers.append('имя: ' + message.text)
	elif n == 2:
		bot.send_message(id, 'Ваш почтовый ящик: ')
		answers.append('телефон: ' + message.text)
	elif n == 3:
		bot.send_message(id, 'Ваш город: ')
		answers.append('почта: ' + message.text)

@bot.message_handler(commands=['start'])
def handle_start(message):
	bot.send_message(message.chat.id, 'Нажмите кнопку "Заполнить заявку"', reply_markup=keyboard1())

def keyboard1():
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	button_1 = types.KeyboardButton('Заполнить заявку')
	markup.add(button_1)
	return markup

@bot.message_handler(content_types=['text'])
def handle_text(message):
	global my_list, n, sost, answers
	if message.text == 'Заполнить Анкету':
		bot.send_message(message.chat.id, 'Заявка: ')
		n = 0
		sost = 1
		answers = []
		if message.chat.username == None:
			answers.append('нет ника')
		else:
			answers.append('@' + message.chat.username)
		bot.send_message(message.chat.id, 'Как вас зовут?')
	else:
		if sost == 1:
			n += 1
			sending(message.chat.id, message)
			
bot.polling(none_stop=True, interval=0)
