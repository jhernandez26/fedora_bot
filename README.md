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


## Configuration
## Security best practice
