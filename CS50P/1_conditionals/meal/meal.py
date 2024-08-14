
def main():
    time_string = str(input("What time is it? "))
    decimal_time = convert(time_string)

    if 7 <= decimal_time <= 8:
        print("breakfast time")
    elif 12 <= decimal_time <= 13:
        print("lunch time")
    elif 18 <= decimal_time <= 19:
        print("dinner time")
    else:
        print(" ")


def convert(time):
    ''' converts formatted string inputs
    ##:## a.m. & ##:## p.m (12-hour times)
    as well as ##:## (24-hour times)
    to a decimal time '''

    if "a.m." in time:
        time = time.replace("a.m.", "").strip()
        hours, minutes = time.split(":")
        hours = int(hours)
        hours -= 12
        minutes = int(minutes)
        am_time_float = hours + (minutes / 60)
        return am_time_float
    elif "p.m." in time:
        time = time.replace("p.m.", "").strip()
        hours, minutes = time.split(":")
        hours = int(hours)
        hours += 12
        minutes = int(minutes)
        pm_time_float = hours + (minutes / 60)
        return pm_time_float
    else:
        hours, minutes = time.split(":")
        hours = int(hours)
        minutes = int(minutes)
        time_float = hours + (minutes / 60)
        return time_float


if __name__ == "__main__":
    main()
