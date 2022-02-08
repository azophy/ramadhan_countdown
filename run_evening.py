from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
from hijri_converter import Hijri, Gregorian

import helper as helper

FORBIDDEN_SHAUM_DATE = [
    # eid al fitr
    [10,1],
    [10,2],
    [10,3],

    # eid al adh
    [12,10],
    [12,11],
    [12,12],
    [12,13],
]

SPECIAL_SHAUM_DATE = [
    # asyuro
    [1,10],

    # arafah days
    [12,8],
    [12,9],
]

"""
count first day of ramadhan & countdown

param
-----

    today: datetime.date object

return
------

    msg: string
"""
def getShaumReminder(today):
    today_gregorian = Gregorian.fromdate(today)
    today_hijri = today_gregorian.to_hijri()
    hijri_year = today_hijri.year

    first_ramadhan = Hijri(hijri_year, 9, 1)
    days_to_ramadahan = (first_ramadhan.to_gregorian() - today).days

    tomorrow = today + timedelta(days=1)
    tomorrow_hijri = Gregorian.fromdate(tomorrow).to_hijri()

    # too close to Ramadhan, or may already in or after Ramadhan
    if today_hijri.month == 9:
        print('Today still ramadhan')
        return

    no_shaum_list = [
        Hijri(hijri_year, item[0], item[1])
        for item in
        FORBIDDEN_SHAUM_DATE
    ]

    # tomorrow is forbidden days for shaum
    if tomorrow_hijri in no_shaum_list:
        print('Tomorrow (',tomorrow_hijri,') is forbidden for shaum')
        return

    msg = ''
    days_mapping = {
        0: 'senin',
        3: 'kamis',
    }

    if tomorrow.weekday() in days_mapping:
        msg = f"Besok adalah hari {days_mapping[tomorrow.weekday()]}. Yuk shaum!"
    elif tomorrow_hijri.day in [13,14,15]:
        msg = f"Besok tanggal {tomorrow_hijri.day} hijriah lho. Shaum ayyamil bidh yuk!"
    if (len(msg) > 0) and days_to_ramadahan in range(5,100):
        msg += f"\n\nHitung-hitung latihan untuk Ramadhan yang tinggal {days_to_ramadahan} hari lagi 😁"

    return msg

if __name__ == '__main__':
    today = datetime.now(ZoneInfo('Asia/Jakarta')).date()
    msg = getShaumReminder(today)

    if len(msg) > 0:
        print(msg)
        helper.sendTelegram(msg)
        helper.postTwitter(msg)

