#coding:utf-8
import telebot
from telebot import types
import pandas as pd
import re
import random
data = pd.read_csv('kinopoisk-top250.csv',sep=',')
client = telebot.TeleBot('')
def clear_msg(text):
    text = text.replace(' ','').lower()
    text = text.replace(';','')
    text = text.replace(',','')
    text = text.replace('ё','е')
    text = text.replace('Ё','е')
    return text

def clean_link(link):
    link = link.replace("'",'')
    return link

jonny='Лучший Джонни Сильверхенд 👻'
genius='Слава создателю 😇'
clown='🤡'
izf='Лучший учитель и создатель изформатики\n✌️'
MO='Лучший учитель и классный руководиель\n👏'
fox='Поблизости обнаружено 12 лис'










#                                                 ПРИВЕТСТВИЕ+ДОБАВЛЕНИЕ КНОПОК

@client.message_handler(func = lambda c: c.text == "старт")
def start(message):
    mess = f'Hello, {message.from_user.first_name}, Какой фильм вы хотите посмотреть?!\n!!!ВНИМАНИЕ!!! вводить полностью название картины!\nПриятного просмотра!\n\nСоздатели: @rfs910 и @egorprileppa'
    client.send_message(message.chat.id, mess, parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn_start = types.InlineKeyboardButton('старт')
    btn_rnd_movie = types.InlineKeyboardButton('случайный фильм')
    btn_rnd_actor = types.InlineKeyboardButton('случайный актер')
    btn_actor = types.InlineKeyboardButton('актер')
    markup.add(btn_start, btn_rnd_movie)
    markup.row(btn_rnd_actor, btn_actor)
    client.send_message(message.chat.id, '👍', reply_markup=markup)





#                                                ФУНКЦИЯ(КНОПКА) РАНДОМНЫЙ ФИЛЬМ
@client.message_handler(func = lambda c: c.text == "случайный фильм")
def rand(message):
    name  = random.choice(data['movie'])
    for i in range(len(data)):
        if clear_msg(name) == clear_msg(data['movie'][i]):
            client.send_message(message.chat.id, f"●  Название: [{data.loc[i][1].replace(';',',')}]({clean_link(data.loc[i][9])})\n●  Год: {data.loc[i][2]}\n●  Страна: {data.loc[i][3]}\n●  Рейтинг: {round(data.loc[i][4],2)}\n●  Режиссер: {data.loc[i][6].replace(';',',')}\n●  Оператор: {data.loc[i][7].replace(';',',')}\n●  Актеры: {data.loc[i][8].replace(';',',')}\n●  Описание: {data.loc[i][5].replace(';','')}\n", parse_mode='Markdown')
            client.send_message(message.chat.id, '🎬  Бесплатный просмотр: https://www.sspoisk.ru/film/'+(re.findall(r'\d+', data.loc[i][9].replace('_',' '))[1])+'/')    





#                                                              РАНДОМНЫЕ АКТЕРЫ

@client.message_handler(func = lambda c: c.text == "случайный актер")
def acrtist(message):
    st_act=[]
    for i in range(len(data)):
        st_act.append(data['actors'][i].split(';'))
    set_actors = list(set([x for l in st_act for x in l]))    
    act = random.choice(set_actors)
    actor = f"Фильмы, в которых играл(а) {act}\n⬇️⬇️⬇️"
    client.send_message(message.chat.id, actor, parse_mode='html')    
    for i in range(len(data)):
        if clear_msg(act) in clear_msg(data['actors'][i]):
            client.send_message(message.chat.id, f"Название: {data.loc[i][1].replace(';',',')}\nРейтинг: {round(data.loc[i][4],2)}")    






@client.message_handler(func = lambda c: c.text == "актер")
def acrtist__1(message):
    what_actor = 'Напишите полное имя актера...\n⬇️⬇️⬇'
    client.send_message(message.chat.id, what_actor, parse_mode='html')





#                                                         РАСПОЗНОВАНИЕ ФИЛЬМОВ


@client.message_handler(content_types=["text"])
def start(message):
    found = False
    for i in range(len(data)):
        if clear_msg(message.text) == clear_msg(data['movie'][i]):
            found = True
            client.send_message(message.chat.id, f"●  Название: [{data.loc[i][1].replace(';',',')}]({clean_link(data.loc[i][9])})\n●  Год: {data.loc[i][2]}\n●  Страна: {data.loc[i][3]}\n●  Рейтинг: {round(data.loc[i][4],2)}\n●  Режиссер: {data.loc[i][6].replace(';',',')}\n●  Оператор: {data.loc[i][7].replace(';',',')}\n●  Актеры: {data.loc[i][8].replace(';',',')}\n●  Описание: {data.loc[i][5].replace(';','')}\n", parse_mode='Markdown')
            client.send_message(message.chat.id, '🎬  Бесплатный просмотр: https://www.sspoisk.ru/film/'+(re.findall(r'\d+', data.loc[i][9].replace('_',' '))[1])+'/')

        elif clear_msg(message.text) in clear_msg(data['actors'][i]):
            found=True
            if clear_msg(message.text) == clear_msg('киану ривз'):
                client.send_message(message.chat.id, jonny, parse_mode='html')
            client.send_message(message.chat.id, f"Название: {data.loc[i][1]}\nРейтинг: {round(data.loc[i][4],2)}")
                
                
                
        elif clear_msg(message.text) == clear_msg('андрей теплов'):
            client.send_message(message.chat.id, genius, parse_mode='html')
            break
        elif clear_msg(message.text) == clear_msg('егор прилепин'):
            client.send_message(message.chat.id, genius, parse_mode='html')
            break
        elif clear_msg(message.text) == clear_msg('иван самойленко'):
            client.send_message(message.chat.id, clown, parse_mode='html')
            break
        elif clear_msg(message.text) == clear_msg('иван васильевич'):
            client.send_message(message.chat.id, izf , parse_mode='html')
            break
        elif clear_msg(message.text) == clear_msg('максим олегович'):
            client.send_message(message.chat.id, MO , parse_mode='html')
            break
        elif clear_msg(message.text) == clear_msg('максим давидюк'):
            client.send_message(message.chat.id, fox , parse_mode='html')
            break
        elif clear_msg(message.text) == clear_msg('вика калмыкова'):
            client.send_message(message.chat.id, 'Главный оператор 10Р ' , parse_mode='html')
            client.send_message(message.chat.id, '📸' , parse_mode='html')
            break
        

    if not found:
        client.send_message(message.chat.id,"Я не понял ваш запрос!")
            
    






           

print('start')
client.polling(none_stop=True)
