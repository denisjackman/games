'''
    case case game
'''
ex1 = 'Www.HackerRank.com'
res1 = 'wWW.hACKERrANK.COM'
ex2 = 'Pythonist 2'
res2 = 'pYTHONIST 2'
ex3 = 'HackerRank.com presents "Pythonist 2".'
res3 = 'hACKERrANK.COM PRESENTS "pYTHONIST 2".'


def swap_case(s):
    '''
        swap case
    '''
    result = ''
    for item in s:
        if item.islower():
            result += item.upper()
        elif item.isupper():
            result += item.lower()
        else:
            result += item
    return result

if __name__ == '__main__':
    print(swap_case(ex1) == res1)
    print(swap_case(ex2) == res2)
    print(swap_case(ex3) == res3)
