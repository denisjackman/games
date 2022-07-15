'''
    scratch code
'''
def power(x, y):
    '''
        power function
    '''
    if y == 0:
        return 1
    return x*power(x, y-1)

# (power(2, 3))
nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
nums = filter(lambda X: X > 1, nums)
# (len(list(nums)))


def print_nums(x):
    '''
        print nums function
    '''
    for item in range(x):
        print(item)
        return

print_nums(10)

for i in range(10):
    if not i % 2 == 0:
        print(i+1)
