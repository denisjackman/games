'''
    code wars test bed
'''
import sys
import math


def change_to_binary(a):
    '''
        add binary function
    '''
    # your code here
    result = ''
    c = ''
    for item in a:
        n = ord(item)
        c = "{0:b}".format(n).zfill(7)
        result += c
        c = ''
    return result


def change_to_code(text):
    result = ''
    code_one = "0 "
    count_one = 0
    store_one = ''
    code_zero = "00 "
    count_zero = 0
    store_zero = ''

    for item in text:
        if item == '1':
            count_one += 1
            store_one += '0'
            if count_zero > 0:
                result += code_zero + store_zero + ' '
                store_zero = ''
                count_zero = 0
        if item == '0':
            count_zero += 1
            store_zero += '0'
            if count_one > 0:
                result += code_one + store_one + ' '
                store_one = ''
                count_one = 0
    if count_zero > 0:
        result += code_zero + store_zero
    if count_one > 0:
        result += code_one + store_one

    return result


def main():
    '''
        main function
    '''
    print(change_to_binary('%'))
    print(change_to_code(change_to_binary('%')))


if __name__ == '__main__':
    main()
