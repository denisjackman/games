# Write a simple parser that will parse and run Deadfish.
#
# Deadfish has 4 commands, each 1 character long:
#
# i increments the value (initially 0)
# d decrements the value
# s squares the value
# o outputs the value into the return array
# Invalid characters should be ignored.
#
# parse("iiisdoso")  ==>  [8, 64]


def parse(inpstr):
    result = []
    count = 0
    for item in inpstr:
        if item == 'i':
            count += 1
        if item == 'd':
            count -= 1
        if item == 's':
            count = count ** 2
        if item == 'o':
            result.append(count)
    return result

print parse("iiisdoso")
