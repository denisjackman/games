def trim(beard):
    root = len(beard)
    counter = 1
    newbeard = []
    for item in beard:
        newhair = []
        for hair in item:
            if counter == root:
                if hair == "...":
                    newhair.append(hair)
                else:
                    newhair.append("...")
            else:
                if hair == "J":
                    newhair.append("|")
                else:
                    newhair.append(hair)
        newbeard.append(newhair)
        counter += 1
    return newbeard

print (trim([["J", '|'], ["J", '|'], ["...", '|']]) == [["|", '|'], ["|", '|'],["...", '...']])
print trim([["J", '|'], ["J", '|'], ["...", '|']])
print (trim([["J", "|", "J"],["J", "|", "|"],["...", "|", "J"]]) == [["|", "|", "|"],["|", "|", "|"],["...", "...", "..."]])
print (trim([["J", "|", "J", "J"],["J", "|", "|", "J"],["...", "|", "J", "|"]]) == [["|", "|", "|", "|"],["|", "|", "|", "|"],["...", "...", "...", "..."]])