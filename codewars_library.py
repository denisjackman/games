'''
    codewars function library
'''


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
    #your code here
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
    print("t1: ", positive_sum([1,2,3,4,5]),15)
    print("t2: ", positive_sum([1,-2,3,4,5]),13)
    print("t3: ", positive_sum([-1,2,3,4,-5]),9)
    print("t1:", array_diff([1,2],[1]),[2])
    print("t2:", array_diff([1,2,2,2,3],[2]),[1,3])
    print("r1:", array_diff([1,2],[1]),[2])
    print("r2:", array_diff([1,2,2],[1]),[2,2])
    print("r3:", array_diff([1,2,2], [2]),[1])
    print("finishing up and closing down:")
    print("Starting thersequence:")
    print('t1:', add_binary(1,1),"10")
    print('t2:', add_binary(5,9),"1110")
    print("r1:", add_binary(1,1),"10")
    print("r2:", add_binary(0,1),"1")
    print("r3:", add_binary(1,0),"1")
    print("r4:", add_binary(2,2),'100')
    print("r5:", add_binary(51,12),"111111")
    print("a1:", add_binary(0,2174483647),"10000001100110111111110010111111")
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


if __name__ == '__main__':
    main()
