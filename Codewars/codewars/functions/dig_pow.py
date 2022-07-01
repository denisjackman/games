def dig_pow(n, p):
    result = -1
    other = 0
    power = p
    # your code

    for letter in str(n):
        other += int(letter) ** power
        power +=1
    number = other / n
    total = n * number
    if total == other:
        result = number
    return result



print dig_pow(89,1)
print dig_pow(695,2)
print dig_pow(46288,3)