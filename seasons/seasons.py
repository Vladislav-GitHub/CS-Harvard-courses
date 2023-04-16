import inflect, sys, re
from datetime import date

p = inflect.engine()

def main():
    birth_date = input('Date of Birth: ') # YYYY-MM-DD
    try:
        year, month, day = check_date(birth_date)
    except:
        sys.exit('Invalid date')
    new_birth_date = date(int(year), int(month), int(day))
    today_date = date.today()

    # Get the difference between dates (in days)
    diff = get_difference(new_birth_date, today_date)

    # Convert days to minutes
    minutes = diff.days * 24 * 60

    # Convert numbers in minutes into words
    answer = p.number_to_words(minutes, andword="")
    print(f'{answer.capitalize()} minutes')


def check_date(birth_date):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_date):
        year, month, day = birth_date.split("-")
        return year, month, day


def get_difference(birth_date, today_date):
    timedelta = today_date - birth_date
    return timedelta


if __name__ == "__main__":
    main()