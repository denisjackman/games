def how_many_times(annual_price, individual_price):
    amount = individual_price
    result = 1
    while amount < annual_price:
        result += 1
        amount += individual_price

    return result
    # code here


print how_many_times(40,15) == 3
print how_many_times(30,10) == 3
print how_many_times(80,15) == 6