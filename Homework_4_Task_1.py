from datetime import datetime

def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        difference = abs((today - given_date).days)
        return difference
    except ValueError:
        return "Невірний формат дати. Використовуйте РРРР-ММ-ДД"

print(get_days_from_today("2020-10-09"))
print(get_days_from_today("2030-01-01"))