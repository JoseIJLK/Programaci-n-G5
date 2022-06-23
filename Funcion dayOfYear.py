def isYearLeap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False
def daysInMonth(year, month):
    if month in [4,6,9,11]:
        return 30
    if month == 2:
        if isYearLeap(year):
            return 29
        return 28
    else:
        return 31
def dayOfYear(year, month, day):
    if isYearLeap(year):
        return 366
    return 365  
print(dayOfYear(2000, 12, 31))
