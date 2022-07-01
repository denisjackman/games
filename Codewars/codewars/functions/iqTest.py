def iq_test(numbers):
    #your code here
    store = numbers.split()

    even = 0
    odd = 0
    for item in store:
        nuitem = int(item)
        if nuitem % 2 == 0:
            even += 1
        else:
            odd += 1

    if odd == 1:
        for item in store:
            suitem = int(item)
            if suitem % 2 != 0:
                return store.index(item)+1
    else:
        for item in store:
            suitem = int(item)
            if suitem % 2 == 0:
                return store.index(item)+1


print iq_test("2 4 7 8 10") == 3
print iq_test("1 2 2") ==1

iq_test("0 2 4 7 8 10")
iq_test("0 1 2 2")