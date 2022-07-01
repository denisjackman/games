def dig_pow(n, p):
    other = 0
    power = p
    # your code

    for letter in str(n):
        other += int(letter) ** power
        power += 1
    number = other / n
    total = n * int(number)
    if total == other:
        result = number
    else:
        result = -1
    return result


print dig_pow(89,1), dig_pow(89, 1) == 1
print dig_pow(92, 1), dig_pow(92, 1) == -1
print dig_pow(46288, 3), dig_pow(46288, 3) == 51
print dig_pow(3456789, 1), dig_pow(3456789, 1) == -1
print dig_pow(3456789, 5), dig_pow(3456789, 5) == -1
print dig_pow(46288, 5), dig_pow(46288, 5) == -1
