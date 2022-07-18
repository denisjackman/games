'''

 Complete the 'print_full_name' function below.

 The function is expected to return a STRING.
 The function accepts following parameters:
  1. STRING first
  2. STRING last

'''
def print_full_name(first, last):
    '''
        print full name
    '''
    # Write your code here
    print(f'Hello {first} {last}! You just delved into python.')


def test_answer():
    assert print_full_name('Ross', 'Taylor') == 'Hello Ross Taylor! You just delved into python.'
