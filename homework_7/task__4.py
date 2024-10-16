import calendar

def day_week(*args):

    dict = {}
    counter = 0

    for i in days:
        dict[i] = counter + 1
        counter += 1
    return dict

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(days)
day_week(days)
print(day_week(days))

def days_week(*args):
    dict = {}
    counter = 0

    for i in days:
        dict[counter + 1] = i
        counter += 1
    return dict

days_week(days)
print(days_week(days))

