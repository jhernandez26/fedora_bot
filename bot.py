#!/opt/fedora_bot/bot_fedora_dependencies/bin/python

# Libraries
## Config parser
import configparser

## Telegram rest-API libraries
import telebot

## Operation system libraries
import platform
import distro
import subprocess

## Regex library
import re

# Workstation class
class workstation_linux:

    ## Workstation atributes
    _information = platform.uname()
    _distribution = distro.name(pretty=True)

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
        return self._distribution + " , " + self._information
        
    ### Run command into linux
    def run_command(self,command):
        out=''
        if command.find('|') != -1:
            proc = {}
            commands = command.split('|')
            size = len(commands)
            i = 0 
            for run in commands:
                key = str("p" + str(i))
                if i == 0:
                    proc[key] = subprocess.Popen([run],stdout=subprocess.PIPE,shell=True)
                elif i != size -1:
                    key_aux = str("p" + str(i -1))
                    proc[key] = subprocess.Popen([run],stdout=subprocess.PIPE,shell=True,stdin=proc[key_aux].stdout)
                else:
                    key_aux = str("p" + str(i -1))
                    output = subprocess.run([run],shell=True, capture_output=True,encoding="utf-8",stdin=proc[key_aux].stdout)
                i = i +1                     
        else:
            output=subprocess.run([command],shell=True, capture_output=True,encoding="utf-8")
        if output.returncode != 0:
            if output.stderr == '':
                out = 'Not found'
            else:
                out = output.stderr
        else:
            out = output.stdout
        return out

print("Starting bot")
pc = workstation_linux()
config_obj = configparser.ConfigParser()
config_obj.read("/etc/fedora_bot/bot.ini")
bot_config = config_obj["bot"]
bot = telebot.TeleBot(bot_config["token"])


# Handler for get messages

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Hello, this bot can control the workstation: " + pc.get_information() )

@bot.message_handler(commands=['pcinformation'])
def send_information(message):
    	bot.reply_to(message, " The workstation is: " + pc.get_information() )

@bot.message_handler(commands=['uptime'])
def send_uptime(message):
    output = pc.run_command("uptime")
    bot.reply_to(message,output)

@bot.message_handler(commands=['date'])
def send_date(message):
    output = pc.run_command("date")
    bot.reply_to(message,output)

@bot.message_handler(commands=['freemem'])
def send_freemem(message):
    output = pc.run_command("free -h")
    bot.reply_to(message,output)

@bot.message_handler(commands=['cpuinfo'])
def send_cpuinfo(message):
    output = pc.run_command("lscpu")
    bot.reply_to(message,output)

@bot.message_handler(commands=['topmem'])
def send_cpuinfo(message):
    output = pc.run_command("top -b -n1   -o %MEM | head  -20")
    bot.reply_to(message,output)

@bot.message_handler(commands=['topcpu'])
def send_cpuinfo(message):
    output = pc.run_command("top -b -n1   -o %CPU | head  -20")
    bot.reply_to(message,output)

@bot.message_handler(commands=['diskspace'])
def send_diskspace(message):
    output = pc.run_command("df -h")
    bot.reply_to(message,output)

@bot.message_handler(commands=['reboot'])
def send_diskspace(message):
    output = pc.run_command("sudo reboot")
    bot.reply_to(message,output)


@bot.message_handler(commands=['isrunning'])
@bot.message_handler(regexp=r"isrunning\s'.*'")
def semd_deamon(message):
    command = 'systemctl list-units --type=service | grep  ' + re.sub(r"/isrunning\s'(.*)'",r"\1",message.text)
    output = pc.run_command(command)
    bot.reply_to(message,output)

@bot.message_handler(commands=["run"])
@bot.message_handler(regexp=r"run\s'.*'")
def run_command(message):
    command = re.sub(r"/run\s'(.*)'",r"\1",message.text)
    output = pc.run_command(command)
    bot.reply_to(message,output)

@bot.message_handler(func=lambda m: True)
def repeat(message):
    bot.send_message(message.chat.id, message.text)

while True:
    try:
        bot.polling()
    except:
        print (0)
    finally:
        pass
    