file = open("books.txt",'r')

item = file.readline()
while item:
    result = item.strip('\n')
    output = result[0]+str(len(result))
    print(output)
    item = file.readline()

file.close()
