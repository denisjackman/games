s = input()
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
digit = '0123456789'
result = ''
for item in s:
    if upper.find(item) > 0:
        result += upper[:upper.find(item)+1]
    if lower.find(item) > 0:
        result += lower[:lower.find(item)+1]
    if digit.find(item) > 0:
        result += digit[:digit.find(item)+1]
print(result )
