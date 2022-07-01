def int_to_english(n):
    #your code here
    result = ""
    SINGLES = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
                  6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
                  11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
                  15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
    TENS = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    UNITS=["hundred","thousand","million","billion","trillion"]

    number = n
    units = n  % 100
    hunits = (n - units) % 1000
    xunits = (n - (units + hunits)) % 1000000
    munits = (n - (units + hunits + xunits)) % 1000000000
    bunits = (n - (units + hunits + xunits + munits)) % 1000000000000
    cunits = (n - (units + hunits + xunits + munits + bunits)) % 1000000000000000

    newunits = units
    newhunits = hunits / 1000
    newxunits = xunits / 1000000
    newmunits = munits / 1000000000
    newbunits = bunits / 1000000000000
    newcunits = cunits / 1000000000000000

    if newunits > 0:
        if newunits < 20:
            result += SINGLES[newunits]


    return result

print int_to_english(1)
print int_to_english(10)
print int_to_english(25161045656) == 'twenty five billion one hundred sixty one million forty five thousand six hundred fifty six'
