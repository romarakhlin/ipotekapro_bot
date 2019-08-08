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
	if n == 19:
		bot.send_message(id,'Спасибо за обращение! Ближайщее время мы свяжемся с Вами')
		answers.append('доп. комментарии: ' + message.text)
		s = ''
		for i in range(len(answers)):
			s += str(answers[i]) + '\n'
		def send_email(addr_from, password, addr_to):
		    msg_subj = 'Новое анкета'
		    msg_text = s
		    msg = MIMEMultipart()
		    msg['From'] = addr_from
		    msg['To'] = addr_to
		    msg['Subject'] = msg_subj

		    body = msg_text
		    msg.attach(MIMEText(body, 'plain'))

		    server = smtplib.SMTP('smtp.gmail.com', 587)
		    server.starttls()
		    server.login(addr_from, password)
		    server.send_message(msg)
		    server.quit()
		_from = 'a9211877427@gmail.com'
		_password = 'Zxcvbnm12:'
		_to = 'contrust24@gmail.com'
		send_email(_from, _password, _to)
		sost = 0
	elif n == 1:
		bot.send_message(id, 'Ваш регион: ')
		answers.append('для кого: ' + message.text)
	elif n == 2:
		bot.send_message(id, 'Ваше имя: ')
		answers.append('регион: ' + message.text)
	elif n == 3:
		bot.send_message(id, 'Ваш почтовый ящик: ')
		answers.append('имя: ' + message.text)
	elif n == 4:
		bot.send_message(id, 'Ваш телефон: ')
		answers.append('почтовый ящик: ' + message.text)
	elif n == 5:
		bot.send_message(id, 'Возраст заёмщика: ')
		answers.append('телефон: ' + message.text)
	elif n == 6:
		bot.send_message(id, 'Пол заёмщика: ', reply_markup=keyboard3())
		answers.append('возраст: ' + message.text)
	elif n == 7:
		bot.send_message(id, 'Гражданство РФ: ', reply_markup=keyboard4())
		answers.append('пол: ' + message.text)
	elif n == 8:
		bot.send_message(id, 'Регистрация заёмщика: ', reply_markup=keyboard5())
		answers.append('гражданство РФ: ' + message.text)
	elif n == 9:
		bot.send_message(id, 'Тип занятости: ', reply_markup=keyboard6())
		answers.append('регистрация: ' + message.text)
	elif n == 10:
		bot.send_message(id, 'Форма подтверждения дохода: ', reply_markup=keyboard7())
		answers.append('тип занятости: ' + message.text)
	elif n == 11:
		bot.send_message(id, 'Общий трудовой стаж, лет: ')
		answers.append('форма подтверждения: ' + message.text)
	elif n == 12:
		bot.send_message(id, 'Стаж на последнем месте работы, мес: ')
		answers.append('общий трудовой стаж, лет: ' + message.text)
	elif n == 13:
		bot.send_message(id, 'Статус недвижимости: ', reply_markup=keyboard8())
		answers.append('стаж на последнем месте работы, мес: ' + message.text)
	elif n == 14:
		bot.send_message(id, 'Цель кредита: ', reply_markup=keyboard9())
		answers.append('статус недвижимости: ' + message.text)
	elif n == 15:
		bot.send_message(id, 'Есть подобранный объект для покупки: ', reply_markup=keyboard10())
		answers.append('цель кредита: ' + message.text)
	elif n == 16:
		bot.send_message(id, 'Стоимость объекта, руб: ')
		answers.append('есть подобранный объект: ' + message.text)
	elif n == 17:
		bot.send_message(id, 'Размер первоначального взноса, руб: ')
		answers.append('стоимость объекта: ' + message.text)
	elif n == 18:
		bot.send_message(id, 'Дополнительные комментарии: ')
		answers.append('размер первоначального взноса: ' + message.text)



@bot.message_handler(commands=['start'])
def handle_start(message):
	bot.send_message(message.chat.id, 'Нажмите кнопку "Заполнить Анкету"', reply_markup=keyboard1())

def keyboard1():
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	button_1 = types.KeyboardButton('Заполнить Анкету')
	markup.add(button_1)
	return markup


@bot.message_handler(content_types=['text'])
def handle_text(message):
	global my_list, n, sost, answers
	if message.text == 'Заполнить Анкету':
		bot.send_message(message.chat.id, 'Анкета: ')
		n = 0
		sost = 1
		answers = []
		if message.chat.username == None:
			answers.append('нет ника')
		else:
			answers.append('@' + message.chat.username)


		bot.send_message(message.chat.id, 'Для кого нужна ипотека?', reply_markup=keyboard2())
	else:
		if sost == 1:
			n += 1
			sending(message.chat.id, message)

def keyboard2():
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	button_1 = types.KeyboardButton('Для себя')
	button_2 = types.KeyboardButton('Я агент, для моего книента')
	markup.add(button_1)
	markup.add(button_2)
	return markup


def keyboard3():
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	button_1 = types.KeyboardButton('Мужской')
	button_2 = types.KeyboardButton('Женский')
	markup.add(button_1)
	markup.add(button_2)
	return markup

def keyboard4():
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	button_1 = types.KeyboardButton('Да')
	button_2 = types.KeyboardButton('Нет')
	markup.add(button_1)
	markup.add(button_2)
	return markup

def keyboard5():
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	button_1 = types.KeyboardButton('Постоянная')
	button_2 = types.KeyboardButton('Временная')
	button_3 = types.KeyboardButton('Отсутствует')
	markup.add(button_1)
	markup.add(button_2)
	markup.add(button_3)
	return markup

def keyboard6():
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	button_1 = types.KeyboardButton('По найму')
	button_2 = types.KeyboardButton('Свой бизнес')
	markup.add(button_1)
	markup.add(button_2)
	return markup

def keyboard7():
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	button_1 = types.KeyboardButton('2НДФЛ')
	button_2 = types.KeyboardButton('По форме банка')
	button_3 = types.KeyboardButton('Без подтверждения')
	markup.add(button_1)
	markup.add(button_2)
	markup.add(button_3)
	return markup

def keyboard8():
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	button_1 = types.KeyboardButton('Строящееся')
	button_2 = types.KeyboardButton('Вторичка')
	markup.add(button_1)
	markup.add(button_2)
	return markup

def keyboard9():
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	button_1 = types.KeyboardButton('Квартира, апартаменты')
	button_2 = types.KeyboardButton('Коммерческая недвижимость')
	button_3 = types.KeyboardButton('Комната')
	button_4 = types.KeyboardButton('Рефинансирование ипотеки')
	button_5 = types.KeyboardButton('Апартаменты')
	button_6 = types.KeyboardButton('Жилой дом с зем. участком')
	markup.add(button_1)
	markup.add(button_2)
	markup.add(button_3)
	markup.add(button_4)
	markup.add(button_5)
	markup.add(button_6)
	return markup

def keyboard10():
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	button_1 = types.KeyboardButton('Да')
	button_2 = types.KeyboardButton('Нет')
	markup.add(button_1)
	markup.add(button_2)
	return markup



bot.polling(none_stop=True, interval=0)
