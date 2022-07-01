#!/usr/bin/python
'''
Write a function that takes in a string of one or more words,
and returns the same string, but with all five or more letter words reversed
(Just like the name of this Kata).
Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.
'''

def spin_words(sentence):
    # Your code goes here
    return None

def spin_words( sentence ):
    result = ""
    tempstr = sentence.split(" ")
    for item in tempstr:
        if len(item) > 4:
            result = result + item[::-1]
        else:
            result = result + item
    return result

if __name__ == '__main__':
    print spin_words("Hello")
    print spin_words("You too")
    print spin_words("me")
    print spin_words("Hello me string to reverse now!")
    print spin_Words("Hey fellow warriors") == " Hey wollef sroirraw"
    print spin_Words("This is a test") == "This is a test"
    print spin_Words("This is another test") == "This is rehtona test"
