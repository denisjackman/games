def getCount(inputStr):
    tempStr = inputStr.lower()
    num_vowels = 0
    count = 0
    count += tempStr.count("a")
    count += tempStr.count("e")
    count += tempStr.count("i")
    count += tempStr.count("o")
    count += tempStr.count("u")
    # your code here
    num_vowels = count
    return num_vowels

print getCount("denis") == 2