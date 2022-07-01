def solution(s):
    result = []
    temp = ""

    if len(s) % 2 != 0:
        s += "_"

    for letter in s:
        temp += letter
        if len(temp) == 2:
            result.append(temp)
            temp = ""
    return result


print solution("asdfasdf")
print solution("asdfads")
print solution("x")
print solution("")