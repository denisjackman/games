'''
    This is a test deb for codewars stuff
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


def main():
    """ This is the main routine for the program """
    print("Starting the sequence:")
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
