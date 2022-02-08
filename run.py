from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from hijri_converter import Hijri, Gregorian

import helper as helper

# count first day of ramadhan & countdown
def sendRamadhanMessage():
    today = datetime.now(ZoneInfo('Asia/Jakarta')).date()
    today_gregorian = Gregorian.fromdate(today)
    today_hijri = today_gregorian.to_hijri()
    hijri_year = today_hijri.year

    first_ramadhan = Hijri(hijri_year, 9, 1)

    days_to_ramadahan = (first_ramadhan.to_gregorian() - today).days

    msg = None
    if days_to_ramadahan in range(1,100):
        msg = f"{days_to_ramadahan} hari menuju Ramadhan {hijri_year} H\n\nApa yang sudah kamu persiapkan untuk Ramadhan kali ini?"
    elif today_hijri.month == 9 : # is currently ramadhan
        msg = f"Hari ke {today_hijri.date} Ramadhan {hijri_year} H. Mari jadikan Ramadhan kali ini Ramadhan terbaik kita selama ini!"

    if msg is not None:
        print(msg)
        helper.sendTelegram(msg)
        helper.postTwitter(msg)

if __name__ == '__main__':
    sendRamadhanMessage()

