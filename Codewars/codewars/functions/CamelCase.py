def to_camel_case(text):
    #your code here
    result = ""
    store = text.replace("_","-")
    newstore = store.split("-")
    counter = 0
    for item in newstore:
        if counter == 0:
            counter += 1
            result += item
        else:
            result += item.capitalize()

    return result



print to_camel_case('')
print to_camel_case("the_stealth_warrior")
print to_camel_case("The-Stealth-Warrior")
print to_camel_case("A-B-C")
