import base64

# It should be fine now. Note that the non-padding version (without = at the end) is used.
# (Reference: https://en.wikipedia.org/wiki/Base64#Implementations_and_history and the examples above that heading)
# https://code.tutsplus.com/tutorials/base64-encoding-and-decoding-using-python--cms-25588
#
# 1.  The text to be encoded in converted into its respective decimal values
#     (http://www.asciitable.com/)
#
# 2.  The decimal values obtained in the above step are converted into their binary equivalents (i.e. 97: 01100001).
#
# 3.  All the binary equivalents are concatenated, obtaining a large set of binary numbers.
#
# 4.  The large set of binary numbers is divided into equal sections, with each section containing only 6 bits.
#
# 5.  The equal sets of 6 bits are converted into their decimal equivalents.
#
# 6.  Finally, the decimal equivalents are converted into their Base64 values (i.e. 4: E).
#     Here are the decimal values and their Base64 alphabet.
#     (https://www.garykessler.net/library/base64.html)
#
# Links
#       http://www.asciitable.com/
#       https://www.base64encode.org/
#       https://tools.ietf.org/html/rfc4648
#       https://www.garykessler.net/library/base64.html
#       https://en.wikipedia.org/wiki/Base64
#       https://code.tutsplus.com/tutorials/base64-encoding-and-decoding-using-python--cms-25588
#       https://www.mathsisfun.com/binary-decimal-hexadecimal-converter.html
#

b64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
r64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
debug = False


def to_base_64(string):
    global debug
    global b64
    n = 6
    nustr = ""
    for char in string:
        if char != ' ':
            nustr += '0'+format(ord(char), 'b')
            if debug:
                print char, '0'+format(ord(char), 'b'), ord(char)
    parts = [nustr[i:i+n] for i in range(0, len(nustr), n)]
    if debug:
        print "\n"
    nustr = ""
    for part in parts:
        nustr += b64[int(part, 2)]
        if debug:
            print b64[int(part, 2)], part, int(part,2)
    if debug:
        print "\n"
    return nustr


strto64 = 'Man is distinguished, not only by his reason, but by this singular passion from other animals, which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable generation of knowledge, exceeds the short vehemence of any carnal pleasure.'
from64tostr = 'TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCBieSB0aGlzIHNpbmd1bGFyIHBhc3Npb24gZnJvbSBvdGhlciBhbmltYWxzLCB3aGljaCBpcyBhIGx1c3Qgb2YgdGhlIG1pbmQsIHRoYXQgYnkgYSBwZXJzZXZlcmFuY2Ugb2YgZGVsaWdodCBpbiB0aGUgY29udGludWVkIGFuZCBpbmRlZmF0aWdhYmxlIGdlbmVyYXRpb24gb2Yga25vd2xlZGdlLCBleGNlZWRzIHRoZSBzaG9ydCB2ZWhlbWVuY2Ugb2YgYW55IGNhcm5hbCBwbGVhc3VyZS4'
st = "Man is"
ast = "Man"
bst = "is"
cst = "ZZZ"

print len(r64), len(b64), b64 == r64, b64.find("M")

print to_base_64(strto64)
print from64tostr
print strto64 == from64tostr
