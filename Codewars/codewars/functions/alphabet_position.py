def alphabet_position(text):
    result = ""
    temp = text.upper()
    r = range(65, 91)
    for letter in temp:
        if (ord(letter) in r):
            result += str(ord(letter) - 64) + " "
    temp = result.strip()
    result = temp
    return result
print alphabet_position("ABCDEF")
print alphabet_position("The sunset sets at twelve o' clock.")
print "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
print alphabet_position("The sunset sets at twelve o' clock.") == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
print alphabet_position("The narwhal bacons at midnight.") == "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20"
