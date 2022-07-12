celsius = int(input())

def conv(c):
    #your code goes here
    result = 0
    result = (9/5 * c + 32)
    return result

fahrenheit = conv(celsius)
print(fahrenheit)
