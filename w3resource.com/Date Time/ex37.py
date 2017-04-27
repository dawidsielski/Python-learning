import datetime

def date_difference(date1, date2):
    """Function returns difference between two dates in seconds"""
    if date2 > date1:
        difference = date2 - date1
    else:
        difference = date1 - date2
    return (difference.days * 24 * 3600 + difference.seconds)


def seconds_to_date(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    return (days, hours, minutes, seconds)

def main():
    
    d1 = datetime.datetime(2017,1,1,0,0,0)
    d2 = datetime.datetime.now()
    print(date_difference(d1,d2))

    print(seconds_to_date(86500))

if __name__ == "__main__":
    main()