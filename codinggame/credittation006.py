s = input()
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
result = ""
input_string = s.split()
result = input_string[0].lower()
item = 1
while item in range(1, len(input_string)):
    temp = input_string[item].lower()
    result += temp.title()
    item += 1
print(result)
