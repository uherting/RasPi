#!/usr/bin/python3

import os
import time
from subprocess import *
import telepot

botName = "TelegramBot"  # your bot name
botToken = "bla"  # your bot token

receiver = [00000000]  # Your telegram address (admin address)

cmdConfirmed = False
cmdHalt = False
cmdReboot = False


def run_cmd(cmd):
    com = Popen(cmd, shell=True, stdout=PIPE)
    shell_output = com.communicate()
    return shell_output[0]


def command_info(ci_id):
    message = "/start: start the bot on your device.\n"
    message += "/info: information about the bot.\n"
    message += "/halt: shutdown the Pi.\n"
    message += "/reboot: cmdReboot the Pi.\n"
    message += "/getip: returns the local network IP address\n"
    Bot.sendMessage(ci_id, message)


def command_get_ip(cgi_id):
    cmd_ip = "ip addr show eth0 | grep inet |awk '{print $2}' | cut -d/ -f1"
    str_ip = run_cmd(cmd_ip).split('\n')[0]
    message = "IP address: " + str_ip
    Bot.sendMessage(cgi_id, message)


def message_handler(msg):
    global cmdConfirmed
    global cmdHalt
    global cmdReboot

    chat_id = msg['chat']['id']
    chat_command = msg['text']

    cmdConfirmed = False
    cmdHalt = False
    cmdReboot = False

    if chat_id in receiver:
        # cmdConfirmed
        if chat_command == "/yes":
            cmdConfirmed = True
        if chat_command == "/no":
            cmdConfirmed = False
            cmdHalt = False
            cmdReboot = False
        # info
        elif chat_command == "/info":
            command_info(chat_id)
        # cmdHalt
        elif chat_command == "/halt":
            cmdHalt = True
            Bot.sendMessage(chat_id, "Shutdown the Pi?")
        # cmdReboot
        elif chat_command == "/reboot":
            cmdReboot = True
            Bot.sendMessage(chat_id, "Reboot the Pi?")
        # getip
        elif chat_command == "/getip":
            command_get_ip(chat_id)
        # error
        else:
            pass

    # Unauthorized access
    else:
        Bot.sendMessage(chat_id, "Access denied.")


if __name__ == "__main__":
    Bot = telepot.Bot(botToken)
    BotInfo = Bot.getMe()
    Bot.message_loop(message_handler)

    time.sleep(1)  # note: if you want pretty and stable code you don't use delays (but i use it anyway)

    for Item in receiver:
        Bot.sendMessage(Item, "Raspberry Pi online.")

    while True:
        if cmdHalt and cmdConfirmed:
            os.system("sudo halt")
        if cmdReboot and cmdConfirmed:
            os.system("sudo reboot")
