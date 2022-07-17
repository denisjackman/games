'''
  split and join function
'''
test1 = 'this is a string'
result1 = 'this-is-a-string'


def split_and_join(inputline):
    '''
        split and join
    '''
    # write your code here
    transtable = inputline.maketrans(' ','-')
    return_result = inputline.translate(transtable)
    return return_result

if __name__ == '__main__':
    print(split_and_join(test1)==result1)
