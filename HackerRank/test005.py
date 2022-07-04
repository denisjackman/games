def is_leap(year):
    result = False

    # Write your logic here
    # your code here. Try to do it in one line.
    if (year % 400 == 0) and (year % 100 == 0):
        result = True
    elif (year % 4 == 0) and (year % 100 != 0):
        result = True
    return result

year = int(input())
