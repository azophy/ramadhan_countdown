from hijri_converter import Hijri, Gregorian

# count first day of ramadhan & countdown
today_hijri = Hijri.today()
hijri_year = today_hijri.year
today_gregorian = Gregorian.today()

first_ramadhan = Hijri(hijri_year, 9, 1)
first_ramadhan_gregorian = first_ramadhan.to_gregorian()

days_to_ramadahan = (first_ramadhan_gregorian - today_gregorian).days

if days_to_ramadahan in range(1,100):
    print(f"{days_to_ramadahan} days until Ramadhan {hijri_year}")
elif today_hijri.month == 9 : # is currently ramadhan
    print(f"Today is day {today_hijri.date} of Ramadhan {hijri_year} AH")


