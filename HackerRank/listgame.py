# if __name__ == '__main__':
N = int(input())
store = []
for item in range(N):
    inputcommand = input()
    command = inputcommand.split()
    if command[0] == 'print':
        print(store)
    if command[0] == 'insert':
        insert_seq = int(command[1])
        insert_data = int(command[2])
        store.insert(insert_seq, insert_data)
    if command[0] == 'remove':
        remove_data = int(command[1])
    if command[0] == 'append':
        append_data = int(command[1])
        store.append(append_data)
    if command[0] == 'sort':
        store.sort()
    if command[0] == 'pop':
        store.pop()
    if command[0] == 'reverse':
        store.reverse()
