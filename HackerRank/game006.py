'''
    mutate-string
'''


def mutate_string(string, position, character):
    '''
        mutate_string function
    '''
    result = ''
    result = string[:position] + character + string[position+1:]
    return result


print(mutate_string('abracadabra',5,'k') == 'abrackdabra')
