"""
Counting Sundays
Problem 19


You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.

    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.

    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

"""

days = ["sun", "mon","tue", "wed", "thur", "fri", "sat"];
month_days = {
    "jan":31, 
    "feb":28, 
    "march":31, 
    "april":30, 
    "may":31, 
    "june ":30, 
    "july":31, 
    "aug":31, 
    "sept":30, 
    "oct":31, 
    "nov":30,
    "dec":31
}
months = month_days.keys()

start_day = "tue"
def isLeapYear(y):
    if y % 4 == 0 and y != 100:
        return True
    elif y % 400 == 0 and y == 100:
        return True
    return False
# days = ["mon","tue", "wed", "thur", "fri", "sat", "sun"];

day_count = 2
sun_count = 0
for y in range(1901, 2001):
    month_days["feb"] = 29 if isLeapYear(y) else 28
    for m in months:
        n_days = month_days[m]
        for i in range(n_days):
            if i == 0 and days[day_count % len(days)] == "sun":
                sun_count += 1
            day_count += 1

end_day = days[day_count % len(days)]
# print(day_count)
print(f"{sun_count=}")

# 448 wrong ! wrong start year !

# 36525 days in these years !
# sun_count=443 WRONG !

# 171 ah shit i thought they meant the first day of the year !
#   current code is extra we dont need to loop over the month_days just add them to day_count