'''
    lesson 005
'''
txt = input()
#your code goes here
str_input= txt.split()
result = max(str_input, key = len)
print(result)
