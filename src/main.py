#!/usr/bin/env python3

import telebot
import re
import config

bot = telebot.TeleBot(config.token)
flag = True


@bot.message_handler(func=lambda message: True, content_types=['text'])
def check_speech(message):
    if check_msg(message.text):
        bot.reply_to(message, make_answer())


def make_answer():
    global flag

    answer = 'Твой дед' if flag else 'Твоя бабка'
    flag = not flag

    return answer


def check_msg(text):
    msg_list = re.findall(r"[\w']+", text)
    msg_list = list(map(str.lower, msg_list))

    return len(set(msg_list) & set(config.trigger_list)) != 0

bot.polling()
