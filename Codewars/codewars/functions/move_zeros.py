def move_zeros(array):
    #your code here
    result = []
    count = 0
    loop = 0
    for item in array:
        if (type(item) == int or type(item) == float) and item == 0:
            count += 1
        else:
            result.append(item)
    for loop in range(0,count):
        result.append(0)
    return result

print move_zeros([0,1,2,3,4,5,6,False,123,0,123,0,12333,1,2,3])