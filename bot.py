#!/opt/fedora_bot/bot_fedora_dependencies/bin/python

# Libraries
## Config parser
import configparser

## Telegram rest-API libraries
import telebot

## Operation system libraries
import platform
import os 
import subprocess

## Regex library
import re

# Workstation class
class workstation:

    ## Workstation atributes
    _information = platform.uname()

    ## Constructor
    def __init__(self):
        self._information = str(self._information)
        self._information = re.sub(r"uname_result\((.*)\)",r"\1",self._information)  # Delete the uname_result() with a regex
        
    ## Destructor
    def __del__(self):
        print("Release PC resources")
    
    ## Workstation methods
    ### Get information about the pc
    def get_information(self):
        return self._information
        
    ### Run command into linux
    def run_command(self,command):
        output=subprocess.run([command],shell=True, capture_output=True,encoding="utf-8")
        return output.stdout


pc = workstation()
config_obj = configparser.ConfigParser()
config_obj.read("/etc/fedora_bot/bot.ini")
bot_config = config_obj["bot"]
bot = telebot.TeleBot(bot_config["token"])
#out = pc.run_command("systemctl status squid")
#print(out)
#del pc



@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Hello, welcome to bot. The workstation information is " + pc.get_information() )


bot.polling()