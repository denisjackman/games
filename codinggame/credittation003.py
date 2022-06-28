word = input()
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
encode = 'abcdefghijklmnopqrstuvwxyz'
decode = 'zyxwvutsrqponmlkjihgfedcba'
word = word.lower()
result = ''
for item in word:
    result += encode[decode.find(item)]
print(result)
