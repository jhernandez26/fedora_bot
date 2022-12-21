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


## Configuration
## Security best practice
