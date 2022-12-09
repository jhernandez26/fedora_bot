#!/opt/fedora_bot/bot_fedora_dependencies/bin/python

# Libraries
## Config parser
import configparser

## Telegram rest-API libraries


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

# Bot class
class bot:

    ## Bot atributes
    pc=''
    token=''

    ## Constructor 
    def __init__(self,token):
        self.pc = workstation()
        self.token = token
    ## Destructor
    def __del__(self):
        del self.pc
        print("Release Bot resources")


def main():
    config_obj = configparser.ConfigParser()
    config_obj.read("/etc/fedora_bot/bot.ini")
    bot_config = config_obj["bot"]
    osbot = bot(bot_config["token"])
    #out = pc.run_command("systemctl status squid")
    #print(out)
    #del pc

if __name__ == "__main__":
    main()

