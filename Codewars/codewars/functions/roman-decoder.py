def solution(roman):
    """
    converts a given string from Roman numerals to an integer
    accepts a string as input and return an integer
    :param string:

    """
    table = [['M', 1000],
             ['CM', 900],
             ['D', 500],
             ['CD', 400],
             ['C', 100],
             ['XC', 90],
             ['L', 50],
             ['XL', 40],
             ['X', 10],
             ['IX', 9],
             ['V', 5],
             ['IV', 4],
             ['I', 1]]
    returnint = 0
    for pair in table:
        continual = True
        while continual:
            if len(roman) >= len(pair[0]):
                if roman[0:len(pair[0])] == pair[0]:
                    returnint += pair[1]
                    roman = roman[len(pair[0]):]
                else:
                    continual = False
            else:
                continual = False
    return returnint