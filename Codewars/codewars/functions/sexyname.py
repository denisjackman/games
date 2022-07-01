SCORES = {'A': 100, 'B': 14, 'C': 9, 'D': 28, 'E': 145, 'F': 12, 'G': 3,
          'H': 10, 'I': 200, 'J': 100, 'K': 114, 'L': 100, 'M': 25,
          'N': 450, 'O': 80, 'P': 2, 'Q': 12, 'R': 400, 'S': 113, 'T': 405,
          'U': 11, 'V': 10, 'W': 10, 'X': 3, 'Y': 210, 'Z': 23}

def sexy_name(name):
    checker = name.upper()
    total = 0
    for letter in checker:
        if letter != " ":
            total += SCORES[letter]
    if total <= 60:
        result = 'NOT TOO SEXY'
    if total >60 and total <= 300:
        result = 'PRETTY SEXY'
    if total >300 and total <= 599:
        result = 'VERY SEXY'
    if total >= 600:
        result = 'THE ULTIMATE SEXIEST'
    return result



'''
       score <= 60:   'NOT TOO SEXY'
 61 <= score <= 300:  'PRETTY SEXY'
301 <= score <= 599:  'VERY SEXY'
       score >= 600:  'THE ULTIMATE SEXIEST'
'''

print sexy_name("denis")
print sexy_name('PHUG')
print sexy_name('BOB')
print sexy_name('YOU')
print sexy_name('ROBBY')
print sexy_name("pamela anderson")