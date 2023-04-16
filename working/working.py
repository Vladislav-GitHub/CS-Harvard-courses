import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if time := re.search(r"^(([\d][\d]*):?([\d][\d])*) ([A-P]M) to (([\d][\d]*):?([\d][\d])*) ([A-P]M)$", s): # 9:00 AM to 5:00 PM
        terms = time.groups()
        if int(terms[1]) > 12 or int(terms[5]) > 12:
            raise ValueError
        first_term = check(terms[1], terms[2], terms[3])
        second_term = check(terms[5], terms[6], terms[7])
        return first_term + ' to ' + second_term
    else:
        raise ValueError


def check(hour, minute, AM_PM):
    if AM_PM == 'PM':
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)
    if minute == None:
        new_minute = '00'
        new_time = f"{new_hour:02}:{new_minute}"
    elif int(minute) >= 60:
        raise ValueError
    else:
        new_time = f"{new_hour:02}:{minute}"
    return new_time


if __name__ == "__main__":
    main()