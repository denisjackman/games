def revrot(strng, sz):
    # your code
    result = ""
    chunks = []
    if sz <= 0:
        return result
    if strng == result:
        return result
    if sz > len(strng):
        return result
    loop = len(strng)/sz
    temp = strng
    for count in range(0,loop):
        chunks.append(temp[:sz])
        tt = temp[sz:]
        temp = tt
    for piece in chunks:
        total = 0
        for digit in piece:
            total += int(digit) ** 3
        if total % 2 == 0:
            result += piece[::-1]
        else:
            result += piece[1:]+piece[:1]


    return result

print revrot("12345",-1) == ""
print revrot("",4) == ""
print revrot("12",4) == ""
print revrot("123456987653", 6) == "234561356789"
print revrot("123456987653", 6)
print revrot("66443875", 4) == "44668753"
print revrot("66443875", 8) == "64438756"
print revrot("664438769", 8) == "67834466"
print revrot("123456779", 8) == "23456771"
print revrot("", 8) == ""
print revrot("123456779", 0) == ""
