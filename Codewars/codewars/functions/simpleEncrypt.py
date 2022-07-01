def decrypt(encrypted_text, n):
    text = encrypted_text
    result = ""
    counter = 0
    while counter in range(0, n):
        half = text[:len(text) / 2]
        other = text[len(text) / 2:]

        while len(other) > len(half):
            half += " "

        result = ""
        loop = 0
        while loop in range(0, len(other)):
            result += other[loop] + half[loop]
            loop += 1
        result.strip()
        text = result
        counter += 1
    return result


def encrypt(text, n):
    if n <= 0:
        return text
    if text == None:
        return text
    if text == "":
        return text
    store = text
    for loop in range(0,n):
        half = ""
        other = ""
        counter = 1
        for letter in store:
            if counter % 2 == 0:
                half += letter
            else:
                other += letter
            counter += 1
        store = half + other
        loop += 1
    return store

'''
print encrypt("This is a test!", 0)=="This is a test!"
print encrypt("This is a test!", 1)=="hsi  etTi sats!"
print encrypt("This is a test!", 2)=="s eT ashi tist!"
print encrypt("This is a test!", 3)==" Tah itse sits!"
print encrypt("This is a test!", 4)=="This is a test!"
print encrypt("This is a test!", -1)=="This is a test!"
print encrypt("This kata is very interesting!", 1)=="hskt svr neetn!Ti aai eyitrsig"
'''

#print decrypt("This is a test!", 0)==  "This is a test!"
print decrypt("hsi  etTi sats!", 1),"This is a test!"
print decrypt("s eT ashi tist!", 2), "This is a test!"
print decrypt(" Tah itse sits!", 3), "This is a test!"
print decrypt("This is a test!", 4), "This is a test!"
#print decrypt("This is a test!", -1), "This is a test!"
print decrypt("hskt svr neetn!Ti aai eyitrsig", 1), "This kata is very interesting!"
