
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    date = input("Date: ").strip()

    if "/" in date:
        # MM/DD/YYYY
        try:
            mm, dd, yyyy =  map(int, date.split("/"))
        except ValueError:
            pass
        else:
            if 0 < mm < 13 and 0 < dd < 32:
                dd = str(dd).zfill(2)
                mm = str(mm).zfill(2)
                print(f"{yyyy}-{mm}-{dd}")
                break

    elif "," in date:
        # Month day, year
        month_name, dd, yyyy = date.split(" ")
        month_name = month_name.title()
        dd = dd.rstrip(",")
        try:
            mm = months.index(month_name) + 1
            dd = int(dd)
        except ValueError:
            pass
        else:
            if 0 < dd < 32:
                dd = str(dd).zfill(2)
                mm = str(mm).zfill(2)
                print(f"{yyyy}-{mm}-{dd}")
                break

