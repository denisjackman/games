def spin_words( sentence ):
    result = ""
    counter = 0
    tempstr = sentence.split(" ")
    for item in tempstr:
        if counter > 0:
            result = result + " "
        if len(item) > 4:
            result = result + item[::-1]
        else:
            result = result + item
        counter += 1
    return result