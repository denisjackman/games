#!/usr/bin/python

'''
Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and
After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter.
When writing on Twitter, he is known for almost always capitalizing every word.

Your task is to convert strings to how they would be written by Jaden Smith.
The strings are actual quotes from Jaden Smith,
but they are not capitalized in the same way he originally typed them.

Example:

Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

Note that the Java version expects a return value of null for an empty string or null.
'''

def toJadenCase(string):
    result = ""
    counter = 0
    tempstr = string.split()
    for item in tempstr:
        if counter > 0:
            result = result + " "
        result = result + item[0].upper() + item[1:]
        counter += 1
    # ...
    return result


print toJadenCase("How can mirrors be real if our eyes aren't real")
