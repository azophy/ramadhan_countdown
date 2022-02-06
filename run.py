import os
import requests
from hijri_converter import Hijri, Gregorian

from dotenv import load_dotenv
load_dotenv()

# count first day of ramadhan & countdown
def getRamadhanCountdownMessage():
    today_hijri = Hijri.today()
    hijri_year = today_hijri.year
    today_gregorian = Gregorian.today()

    first_ramadhan = Hijri(hijri_year, 9, 1)
    first_ramadhan_gregorian = first_ramadhan.to_gregorian()

    days_to_ramadahan = (first_ramadhan_gregorian - today_gregorian).days

    if days_to_ramadahan in range(1,100):
        return f"{days_to_ramadahan} days until Ramadhan {hijri_year}"
    elif today_hijri.month == 9 : # is currently ramadhan
        return f"Today is day {today_hijri.date} of Ramadhan {hijri_year} AH"

# send telegram bot
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
ROOT_BOT_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

res = requests.get(ROOT_BOT_URL + '/sendMessage', json={
    'chat_id': TELEGRAM_CHAT_ID,
    'text': getRamadhanCountdownMessage(),
})
