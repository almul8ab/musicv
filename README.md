
## Heroku Deployment 💜
The easy way to host this bot, deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/kurd-bots/musicar)



## Vps 

`sudo apt update && apt upgrade -y`

`sudo apt install git curl python3-pip ffmpeg -y`

`pip3 install -U pip`

`curl -sL https://deb.nodesource.com/setup_16.x | bash -`

`sudo apt-get install -y nodejs`

`npm i -g npm`

`git clone https://github.com/kurd-bots/musicar` # Clone your repo.

`cd musicar ` #name repo

`pip3 install -U -r requirements.txt`

`cp example.env .env` #Use vim to edit ENVs

`vim .env` #Fill up your ENVs ( Steps press i to enter in insert mode then edit the file. Press Esc to exit the editing mode then type :wq! and press Enter key to save the file.)

`python3 main.py` # Run the bot
