import datetime

def inputDate(date):
    dateStr = input(date)
    return datetime.datetime.strptime(dateStr, '%Y-%m-%d')
date1 = inputDate("Enter the first date (YYYY-MM-DD): ")
date2 = inputDate("Enter the second date (YYYY-MM-DD): ")
date3 = date2 - date1
seconds = date3.total_seconds()

print("Difference in seconds: ", abs(seconds))