<h1 align=center>
    <br/>
    <img src=".\img\IMG-20200219-WA0033.jpg">
    <br/>
    RaMu - Discord Bot
</h1>

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![HitCount](http://hits.dwyl.com/cannibalcheeseburger/Ramu-Discord-bot.svg)](http://hits.dwyl.com/cannibalcheeseburger/Ramu-Discord-bot)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)
[![Made](https://img.shields.io/badge/Made%20With-Python%203.7-green.svg?style=for-the-badge")](https://www.python.org/downloads/)
[![Discord.py](https://img.shields.io/badge/discord-bot-blue.svg)](https://discord.com/api/oauth2/authorize?client_id=715204457754787952&permissions=8&scope=bot)


This repo consists of code put into making RaMu (RanginMuthail). RaMu does some very random and useless tasks.Procede with caution.

Link to invite RaMu to your Discord Server: [RaMu](https://discord.com/api/oauth2/authorize?client_id=715204457754787952&permissions=8&scope=bot)

## Installation

### Python
Bot is written in [Python 3.7.6](https://www.python.org/downloads/)
 
### Build from source

```
git clone https://github.com/cannibalcheeseburger/RaMu-Discord-bot.git

cd RaMu-Discord-bot
```

### Dependencies:

Install the required dependencies preferably in a virtual environment.

```
python -m pip install -r requirements.txt
```

### Run Bot

```
python bot.py
```

__Note__: For obvious reasons TOKEN for bot saved in separate file has not been uploaded. So bot won't work on your machine . 

If you just want it to make your own bot, then replace `creds.TOKEN` in:
```python
client.run(creds.TOKEN)
```
at the end of file `bot.py`.

And remove the line:

```python 
import creds
```

## Usage 

 - Add the bot to your Discord Server : [RaMu](https://discord.com/api/oauth2/authorize?client_id=715204457754787952&permissions=8&scope=bot)
 
 - Type  `--help` on the text channel.

Example of --help:
 ```
 ​No Category:
  --8ball Return a response to the question
  --clear  Clears x number of messages
  --help   Shows this message
  --oobhai Returns maro mujhe maro x number of times
  --ping   Returns Ping
  --recipe Returns recipe of the day
Type --help command for more info on a command.
You can also type --help category for more info on a category.
 ```

 ![Screenshot](./img/screen.png)


 ## APIs

  - [Food API](https://rapidapi.com/spoonacular/api/recipe-food-nutrition) : Used to retrieve recipe of the day.