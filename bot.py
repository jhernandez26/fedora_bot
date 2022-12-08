# Libraries

## Telegram rest-API libraries


## Operation system libraries
import platform
import os 
import subprocess

## Regex library
import re

class workstation:

    # Workstation atributes
    _information = platform.uname()

    # Constructor
    def __init__(self):
        self._information = str(self._information)
        self._information = re.sub(r"uname_result\((.*)\)",r"\1",self._information)
        
    
    # Destructor
    def __del__(self):
        print("Release PC resources")
    
    # Workstation methods
    def get_information(self):
        return self._information
    
    def run_command(self,command):
        output=subprocess.run([command],shell=True, capture_output=True,encoding="utf-8")
        return output.stdout
#
#class bot:
#
#    # Bot atributes
#    pc=''
#
#    # Constructor 
#    def __init__(self):
#        self.pc = workstation()
#    
#    # Destructor
#    def __del__(self):
#        del self.pc
#        print("Release Bot resources")
#
def main():
    pc = workstation()
    out = pc.run_command("systemctl status squid")
    print(out)
    del pc

if __name__ == "__main__":
    main()

