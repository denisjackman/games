'''
    codewars function library
'''


def to_roman(num):
    '''
        cobvert integer to roman
    '''
    num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
               (100, 'C'), (90, 'XC'),(50, 'L'), (40, 'XL'), (10, 'X'),
               (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    roman = ''
    while num > 0:
        for i, r in num_map:
            while num >= i:
                roman += r
                num -= i

    return roman


def NU_to_roman(number):
    '''
        TODO
    '''
    num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    item = 12
    result = ''
    while number:
        div = number // num[item]
        number %= num[item]

        while div:
            result += sym[item]
            div -= 1
        item -= 1
    return result


def from_roman(roman_num):
    """
        :type s: str
        :rtype: int
    """
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    item = 0
    num = 0
    while item < len(roman_num):
        if item + 1 < len(roman_num) and roman_num[item:item+2] in roman:
            num += roman[roman_num[item:item+2]]
            item += 2
        else:
            num += roman[roman_num[item]]
            item += 1
    return num


def decrypt(encrypted_text, n):
    '''
        decryption function
    '''
    result = encrypted_text
    counter = 0
    if n <= 0 or encrypted_text == '':
        return result
    while counter in range(0, n):
        looper = int(len(result)/2)
        if len(result) % 2 == 0:
            slooper = looper
        else:
            slooper = looper + 1

        first_string = result[0:looper]
        second_string = result[looper:]
        result = ""
        for _ in range(0, looper):
            result += second_string[_] + first_string[_]
        if looper < slooper:
            result += second_string[-1]
        counter += 1
    return result


def encrypt(text, n):
    '''
        encryption function
    '''
    result = text
    counter = 0
    if n <= 0 or text == '':
        return result
    while counter in range(0, n):
        second_string = ''
        first_string = ''
        for letter in range(0, len(result)):
            if letter % 2 == 0:
                second_string += result[letter]
            else:
                first_string += result[letter]
        result = first_string + second_string
        counter += 1
    return result


def isLeapYear(year):
    '''
        function is it a leap year
    '''
    result = False
    # your code here. Try to do it in one line.
    if (year % 400 == 0) and (year % 100 == 0):
        result = True
    elif (year % 4 == 0) and (year % 100 != 0):
        result = True
    return result


def array_diff(a, b):
    '''
        array difference fucntion
    '''
    # your code here
    c = a
    for _ in c:
        for check in b:
            while c.count(check) > 0:
                c.remove(check)
    return c


def add_binary(a, b):
    '''
        add binary function
    '''
    # your code here
    n = a + b
    c = "{0:b}".format(n)
    return c


def remove_char(s):
    '''
        remove character function
    '''
    # your code here
    return s[1:len(s)-1]


def positive_sum(arr):
    '''
        positive sum function
    '''
    # Your code here
    result = 0
    for item in arr:
        if item > 0:
            result = result + item
    return result


def repeat_str(repeat, string):
    '''
        repeat str function
    '''
    s = ''
    for _ in range(0, repeat):
        s = s + string
    return s


def main():
    """ This is the main routine for the program """
    print("Starting the sequence:")
    print("t1: ", positive_sum([1, 2, 3, 4, 5]), 15)
    print("t2: ", positive_sum([1, -2, 3, 4, 5]), 13)
    print("t3: ", positive_sum([-1, 2, 3, 4, -5]), 9)
    print("t1:", array_diff([1, 2], [1]), [2])
    print("t2:", array_diff([1, 2, 2, 2, 3], [2]), [1, 3])
    print("r1:", array_diff([1, 2], [1]), [2])
    print("r2:", array_diff([1, 2, 2], [1]), [2, 2])
    print("r3:", array_diff([1, 2, 2], [2]), [1])
    print("finishing up and closing down:")
    print("Starting thersequence:")
    print('t1:', add_binary(1, 1), "10")
    print('t2:', add_binary(5, 9), "1110")
    print("r1:", add_binary(1, 1), "10")
    print("r2:", add_binary(0, 1), "1")
    print("r3:", add_binary(1, 0), "1")
    print("r4:", add_binary(2, 2), '100')
    print("r5:", add_binary(51, 12), "111111")
    print("a1:", add_binary(0, 2174483647), "10000001100110111111110010111111")
    print("a1:",)

    print("t1: ", remove_char('eloquent'), 'loquen')
    print("t2: ", remove_char('eloquent'), 'loquen')
    print("t3: ", remove_char('eloquent'), 'loquen')
    print("t4: ", remove_char('country'), 'ountr')
    print("t5: ", remove_char('person'), 'erso')
    print("t6: ", remove_char('place'), 'lac')
    print("t7: ", remove_char('ok'), '')
    print("t8: ", remove_char('ooopsss'), 'oopss')

    print(repeat_str(4, 'a'), 'aaaa')
    print(repeat_str(3, 'hello '), 'hello hello hello ')
    print(repeat_str(2, 'abc'), 'abcabc')
    print("finishing up and closing down:")

    print('Leap years (should equal True)')
    print(isLeapYear(1984), True, 'Year 1984 was a leap year!')
    print(isLeapYear(2000), True, 'Year 2000 was a leap year!')

    print('Normal years (should equal False)')
    print(isLeapYear(1234), False, 'Year 1234 was NOT a leap year!')
    print(isLeapYear(1100), False, 'Year 1100 was NOT a leap year!')

    print("encrypt:", encrypt("012345", 1), "135024")
    print("encrypt:", encrypt("012345", 0), "012345")
    print("encrypt:", encrypt('', 12), '')
    print("encrypt:", encrypt("01234", 2), "32104")
    print("encrypt:", encrypt("01234", 3), "20314")
    print("decrypt:", decrypt("012345", 0), "012345")
    print("decrypt:", decrypt("", 12), "")
    print("decrypt:", decrypt("135024", 1), "012345")

    print('Basic Tests')
    print("encrypt:", encrypt("This is a test!", 0), "This is a test!")
    print("encrypt:", encrypt("This is a test!", 1), "hsi  etTi sats!")
    print("encrypt:", encrypt("This is a test!", 2), "s eT ashi tist!")
    print("encrypt:", encrypt("This is a test!", 3), " Tah itse sits!")
    print("encrypt:", encrypt("This is a test!", 4), "This is a test!")
    print("encrypt:", encrypt("This is a test!", -1), "This is a test!")
    print("encrypt:", encrypt("This kata is very interesting!", 1), "hskt svr neetn!Ti aai eyitrsig")

    print("decrypt:", decrypt("This is a test!", 0), "This is a test!")
    print("decrypt:", decrypt("hsi  etTi sats!", 1), "This is a test!")
    print("decrypt:", decrypt("s eT ashi tist!", 2), "This is a test!")
    print("decrypt:", decrypt(" Tah itse sits!", 3), "This is a test!")
    print("decrypt:", decrypt("This is a test!", 4), "This is a test!")
    print("decrypt:", decrypt("This is a test!", -1), "This is a test!")
    print("decrypt:", decrypt("hskt svr neetn!Ti aai eyitrsig", 1), "This kata is very interesting!")

    print('testing from roman to integer')
    print("III", 3, from_roman('III'), from_roman('III') == 3)
    print("CDXLIII", 443, from_roman('CDXLIII'), from_roman('CDXLIII') == 443)
    print("MMMDXLIX", 3549, from_roman('MMMDXLIX'), from_roman('MMMDXLIX') == 3549)
    print('testing from integer to roman')
    print("III", 3, to_roman(3), to_roman(3) == 'III')
    print("CDXLIII", 443, to_roman(443), to_roman(443) == 'CDXLIII')
    print("MMMDXLIX", 3549, to_roman(3549), to_roman(3549) == 'MMMDXLIX')


if __name__ == '__main__':
    main()
