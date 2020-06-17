#!/usr/bin/python
# -*- coding: utf8 -*-
from telegram.ext import Updater, CommandHandler
from telegram.error import (TelegramError, Unauthorized, BadRequest, 
                            TimedOut, ChatMigrated, NetworkError)
import logging, random

# admins

admins = [id, id]

# chat id

WORK_GROUP_ID = group_id
TEST_GROUP_ID = group_id

# define commands

def roll(bot, update):
    if update.message.from_user.id not in admins:
        return

    file = open('list.txt', 'r')
    names = file.readlines()
    file.close()

    selection = random.sample(names, 2)
    selection = map(lambda x: x.strip(), selection)
    message = "Подборка:\n" + ",\n".join(selection)
    reply_to_group(update, bot, message)

def get_id(bot, update):
    reply(update, "Ваш id: " + str(update.message.from_user.id))

def get_group_id(bot, update):
    if update.message.from_user.id not in admins:
        return

    send_private_message(update, bot, "Group id: " + str(update.message.chat.id))


# methods

def send(bot, message, parse_mode="Markdown"):
    return


def reply(update, message):
    update.message.reply_text(message)

    
def reply_to_group(update, bot, message):
    bot.send_message(TEST_GROUP_ID, message)


def send_private_message(update, bot, message):
    bot.send_message(update.message.from_user.id, message)


def error_callback(bot, update, error):
    print(error)

# bot setup

updater = Updater(token='BOT_TOKEN')
logging.basicConfig(level=logging.WARN, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
updater.dispatcher.add_error_handler(error_callback)

# add commands

updater.dispatcher.add_handler(CommandHandler('roll', roll))
updater.dispatcher.add_handler(CommandHandler('getid', get_id))
updater.dispatcher.add_handler(CommandHandler('getgroupid', get_group_id))

# launch

updater.start_polling()
updater.idle()
