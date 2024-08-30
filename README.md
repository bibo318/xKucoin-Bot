#  xKucoin-Bot
- Soft for https://t.me/xkucoinbot

## Functionality
> * Functional                        	Supported
> * Multithreading		                ✅
> * Binding a proxy to a session      	✅
> * Login	                            ✅
> * Random sleep time between accounts	✅
> * Support pyrogram .session         	✅
> * Get statistics for all accounts   	✅

## Settings data/config.py
 
> * API_ID / API_HASH   	Platform data from which to launch a Telegram session (stock - Android)
> * DELAYS-ACCOUNT      	Delay between connections to accounts (the more accounts, the longer the delay) (eg [5, 15])
> * PROXY_TYPES-TG      	Proxy type for telegram session (eg 'socks5')
> * PROXY_TYPES-REQUESTS	Proxy type for requests (eg 'socks5')
> * WORKDIR	                directory with session (eg "sessions/")
> * TIMEOUT                	timeout in seconds for checking accounts on valid (eg 30)



## Requirements
* Python 3.9 (you can install it here)
* Telegram API_ID and API_HASH (you can get them here)

**Install the required dependencies:**
> pip install -r requirements.txt

**Usage**

Run the bot:
> python3 main.py