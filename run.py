import os
from datetime import datetime
import requests
from hijri_converter import Hijri, Gregorian

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

# count first day of ramadhan & countdown
def sendRamadhanMessage():
    today_hijri = Hijri.today()
    hijri_year = today_hijri.year
    today_gregorian = Gregorian.today()

    first_ramadhan = Hijri(hijri_year, 9, 1)
    first_ramadhan_gregorian = first_ramadhan.to_gregorian()

    days_to_ramadahan = (first_ramadhan_gregorian - today_gregorian).days

    msg = None
    if days_to_ramadahan in range(1,100):
        msg = f"{days_to_ramadahan} hari menuju Ramadhan {hijri_year} H\n\nApa yang sudah kamu persiapkan untuk Ramadhan kali ini?"
    elif today_hijri.month == 9 : # is currently ramadhan
        msg = f"Hari ke {today_hijri.date} Ramadhan {hijri_year} H. Mari jadikan Ramadhan kali ini Ramadhan terbaik kita selama ini!"

    if msg is not None:
        sendTelegram(msg)
        postTwitter(msg)

if __name__ == '__main__':
    sendRamadhanMessage()

