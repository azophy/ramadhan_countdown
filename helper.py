import os
import requests

try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    print('failed importing dotenv module. skipping...')

# send telegram bot
def sendTelegram(msg):
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
    TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
    ROOT_BOT_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

    return requests.get(ROOT_BOT_URL + '/sendMessage', json={
        'chat_id': TELEGRAM_CHAT_ID,
        'text': msg,
    })

# post to twitter with IFTTT
def postTwitter(msg):
    IFTTT_TWITTER_EVENT_NAME = os.getenv('IFTTT_TWITTER_EVENT_NAME')
    IFTTT_TWITTER_API_KEY = os.getenv('IFTTT_TWITTER_API_KEY')
    IFTTT_TWITTER_TRIGGER_URL = f"https://maker.ifttt.com/trigger/{IFTTT_TWITTER_EVENT_NAME}/with/key/{IFTTT_TWITTER_API_KEY}"

    return requests.post(IFTTT_TWITTER_TRIGGER_URL, {
        'value1': msg,
    })

