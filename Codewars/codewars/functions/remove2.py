def remove(s, n):
    result = ""
    counter = 0
    for letter in s:
        if letter == "!":
            if counter < n:
                result += ""
                counter += 1
            else:
                result += letter
        else:
            result+= letter
    return result