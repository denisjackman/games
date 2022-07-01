#!/usr/bin/python
import datetime

FIRSTNAME = {'January': "The Evil", 'February': "The Vile,", 'March': "The Cruel", 'April': "The Trashy", 'May':"The Despicable", 'June':"The Embarrassing", 'July': "The Disreputable", 'August': "The Atrocious", 'September': "The Twirling", 'October': "The Orange", 'November': "The Terrifying", 'December': "The Awkward"}
LASTNAME = {'0': "Mustache", '1': "Pickle", '2': "Hood Ornament", '3': "Raisin", '4': "Recycling Bin", '5': "Potato", '6': "Tomato", '7': "House Cat", '8': "Teaspoon", '9': "Laundry Basket"}

def  getVillainName(birthday):
    result = ""

    result = FIRSTNAME[birthday.strftime("%B")] + " "
    result += LASTNAME[birthday.strftime("%d")[1]]
    return result



d1 = datetime.date(1965, 11, 18)
print getVillainName(d1)