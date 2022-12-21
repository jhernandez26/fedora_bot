# Telegram linux bot
Telegram bot is an python application for run commands into a Linux pc.


![OpenRepo Demo Video](https://github.com/jhernandez26/fedora_bot/blob/developer/documentacion/img/demo.gif?raw=true)

## Getting Started
The application is working with a token from ** BothFather ** and the ** ChatID **. About the dependencies the python is working with a virtual enviroment.

### Create a token with bothfather
Search the BotFather    


![BotFather search](https://github.com/jhernandez26/fedora_bot/blob/developer/documentacion/img/telegram_1.png)

Run the command **/newbot** and copy the API token

![BotFather search](https://github.com/jhernandez26/fedora_bot/blob/developer/documentacion/img/telegram_3.png)

### Get chat id
From [Telegram Web](https://web.telegram.org/z/), go to the chat and the URL get the ID (the numbers after the # )

![Chat ID](https://github.com/jhernandez26/fedora_bot/blob/developer/documentacion/img/chat_id.png)

## Command
The bot has this commands:

start  - Start bot
pcinformation - Get information about the workstation
uptime - Get workstation uptime
date - Get workstation  date
freemem - Get memory information
cpuinfo - Get CPU information
diskspace - Get disk usasege
reboot - Reboot workstation
isrunning - Check if a deamon is running, example /isrunning 'sshd'
run - Run a command, the command should '', example /run 'ls'
topmem -  Top order by Mem
topcpu - Top order by CPU
reboot_bot - Reboot the bot client
check_kerberos_ticket -  Check kerberos ticket
create_kerberos_ticket - Create a new kerberos ticket

## Installation
### RPM
Download the rpm file from this repositorie, as root user run install the RPM

    # dnf install bot_telegram-1.1.1-1.fc37.x86_64.rpm

>**Note**
>The RPM only works for Fedora 37, the expect is in this repositorie for create a new rpm if you needed.

### Manually

Clone the repositorie 

    $ git clone https://github.com/jhernandez26/fedora_bot.git

Create a user for run the python script
>**Note**
>The RPM create the user usr_srvc_bot

As root move the directory **fedora_bot** to **/opt** 

    # mv fedora_bot /opt

Create the directories **/etc/fedora_bot** and **/var/log/fedora_bot**

    # mkdir -p /etc/fedora_bot /var/log/fedora_bot
mv **bot.ini** to **/etc/fedora_bot**, **bot** to **/etc/logrotate.d** and **bot-telegram.service** to  **/usr/lib/systemd/system**

    # mv bot.ini /etc/fedora_bot
    # mv bot /etc/logrotate.d
    # mv bot-telegram.service /usr/lib/systemd/system

change the owner for the directories **/etc/fedora_bot** and **/opt/fedora_bot**

    # chown <bot_user>:<bot_user> -R /etc/fedora_bot /opt/fedora_bot

Configure the **chat id** and **BotFather token** in **/etc/fedora_bot/bot.ini**
## Configuration
The sections **bot** and **log** are  mandatory.

### Bot configuration ###
In this secction you have to put the API token (**token**)  and the (**chat id**)

### Log configuration ###
The bit has two logs, the **audit** save the commands that run the bot, **log** is the error log for the bot, **loggin** is the log level.

### Kerberos ###
This options is optional, if the workstation is using kerberos or Free Ipa, you can create a kerberos ticket with the command **create_kerberos_ticket**.

The command is using a keytab set in the option **keytab**

## Security best practice
The bot can run any command, as best practice the bot **does not run with root**, however the recomendation is set a sudo rules for set what commands you can run as root or another user.