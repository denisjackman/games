# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
number = n
result = 0
input_string = str(number)
for item in input_string:
    if int(item) % 2 == 0:
        result += int(item)
print(result)
