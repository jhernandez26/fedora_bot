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
import time
from datetime import datetime

## Regex library
import re

## Logging library
import logging

# Global variables

# Workstation class
class workstation_linux:

    ## Workstation atributes
    _information = platform.uname()
    _distribution = distro.name(pretty=True)
    _audit_log = ''

    ## Constructor
    def __init__(self,audit,log_file):
        self._information = str(self._information)
        self._information = re.sub(r"uname_result\((.*)\)",r"\1",self._information)  # Delete the uname_result() with a regex
        self._audit_log = audit + "/audit.log"
        logging.info("The PC "+ self._information+ " is starting to execute.")
        logging.info("The adit los is creating in "+ self._audit_log + ".")
        logging.info("The bot log is in "+ log_file)


    ## Destructor
    def __del__(self):
        print("Release PC resources")
    
    ## Workstation methods
    ### Get information about the pc
    def get_information(self):
        return self._distribution + " , " + self._information
        
    ### Run command into linux
    def run_command(self,command):
        now = datetime.now()
        insert = str(now) + " The bot run the command: " + command + "\n"
        f = open(self._audit_log, 'a')
        f.write(insert)
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

# App configurartion class
class app_configuration:

    ## app_configuration atributes
    ### Private attributes
    _config_obj = ''
    _bot_config = ''
    _log_config = ''
    _kerberos = ''

    ### Public attriebutes
    keytab = 'noconfig'
    audit = 'noconfig'
    token = 'noconfig'
    chat_id = 'noconfig'
    log_file = 'noconfig'
    log_level = 'noconfig'

    ## Constructor
    def __init__(self):
        self._config_obj = configparser.ConfigParser()
        self._config_obj.read("/etc/fedora_bot/bot.ini")
        self._bot_config = self._config_obj["bot"]
        self._log_config = self._config_obj["log"]
        self.log_file = self._log_config["log"] + "/bot.log"
        self.log_level = self._log_config["loggin"]
        self.chat_id = self._bot_config["chat_id"]
        self.audit = self._log_config["audit"]
        self.token = self._bot_config["token"]
        if self._config_obj.has_option("kerberos", "keytab"):
            self._kerberos = self._config_obj["kerberos"]
            self.keytab = self._kerberos["keytab"]
            



conf = app_configuration()
logging.basicConfig(filename=conf.log_file, filemode='w', format='%(asctime)s  %(name)s  %(levelname)s  %(message)s', level=conf.log_level)
logging.info("The bot was started.")
pc = workstation_linux(conf.audit,conf.log_file)
bot = telebot.TeleBot(conf.token )
uptime = pc.run_command("uptime -p | grep -v hours | awk '{print $2}'")
uptime = uptime.rstrip("\n")
msg = 'The bot has been rebooted'
if    uptime != ''  and int(uptime) < 3:
        msg = "The workstation has been rebooted ;)."
while True:
    try:
        bot.send_message(conf.chat_id,msg)
        break
    except Exception as e:
        logging.error("Unexpected error, ",exc_info=True)
        time.sleep(60)
    finally:
        pass
    

# Handler for get messages

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Hello, this bot can control the workstation: " + pc.get_information() )

@bot.message_handler(commands=['check_kerberos_ticket'])
def send_welcome(message):
    output = pc.run_command("klist")
    bot.reply_to(message,output)

@bot.message_handler(commands=['create_kerberos_ticket'])
def send_welcome(message):
    if conf.keytab != 'noconfig':
        command = "kdestroy -A ;kinit -t " +  str(conf.keytab) + " usr_srvc_bot -k;klist"
        output = pc.run_command(command)
        bot.reply_to(message,output)
    else:
        bot.reply_to(message,"You don't have configure a keytab")        

@bot.message_handler(commands=['pcinformation'])
def send_information(message):
    	bot.reply_to(message, " The workstation is: " + pc.get_information() )

@bot.message_handler(commands=['uptime'])
def send_uptime(message):
    output = pc.run_command("uptime -p")
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

@bot.message_handler(commands=['reboot_bot'])
def send_diskspace(message):
    output = pc.run_command("sudo systemctl restart bot-telegram")
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
    bot.send_message(message, message.text)

while True:
    try:
        bot.polling(none_stop=False)
    except Exception as e:
        logging.error("Unexpected error, ",exc_info=True)
        time.sleep(60)
    finally:
        pass
    