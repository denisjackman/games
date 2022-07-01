def find_even_index(arr):
    b = sum(arr) / 2
    c = 0
    d = 0
    for item in arr:
        if c > b:
            d += item
        else:
            c += item
    e = c - d
    if e in arr:
        result = arr.index(e)
    else:
        result = -1
    return result


'''
print 1,find_even_index([1,2,3,4,3,2,1]) == 3
print 2,find_even_index([1,100,50,-51,1,1]) == 1
print 3,find_even_index([1,2,3,4,5,6]) == -1
'''
print 4,find_even_index([20,10,30,10,10,15,35]) == 3
'''print 5,find_even_index([20,10,-80,10,10,15,35]) == 0
print 6,find_even_index([10,-80,10,10,15,35,20]) == 6
'''
print 7,find_even_index(range(1,100)) == -1
'''
print 8,find_even_index([0,0,0,0,0]) == 0
'''
print 9,find_even_index([-1,-2,-3,-4,-3,-2,-1]) == 3
'''
print 0,find_even_index(range(-100,-1)) == -1
'''