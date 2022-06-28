n = int(input())
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
result = 0
for loop in range (1, n+1):
    if loop % 7 == 0:
        result += 1
    elif str(loop).find('7')+1 > 0:
        result += 1
    else:
        count = 0
        for item in str(loop):
            count += int(item)
        if count % 7 == 0:
            result += 1
    print(loop, result, file=sys.stderr, flush=True)
