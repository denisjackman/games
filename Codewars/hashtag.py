# Here's the deal:
#
# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.
# Examples
# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  =>  "#HelloWorld"
# ""                                        =>  false

def generate_hashtag(s):
    # your code here
    t= ""
    if s == "":
        return False

    r = s.split(" ")
    for item in r:
        if item != "":
            t += str(item).title()
    result = "#"
    for char in t:
        if char != " ":
            result += char
    if len(result) > 140:
        return False
    return result

def generate_hashtag(s):
    ans = '#'+ str(s.title().replace(' ',''))
    return s and not len(ans)>140 and ans or False

print generate_hashtag(" Hello there thanks for trying my Kata"), "#HelloThereThanksForTryingMyKata"
print generate_hashtag("    Hello     World   "), "#HelloWorld"
print generate_hashtag(""), False
print generate_hashtag("asdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdf"), False

