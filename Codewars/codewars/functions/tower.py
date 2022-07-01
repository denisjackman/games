def tower_builder(n_floors):
    # build here
    list = []
    result = []
    loop = 1
    tower = "*"
    while loop <= n_floors:
        list.append(tower)
        loop += 1
        tower = "*" + tower + "*"

    note = len(list[-1])
    for item in list:
        temp = '{{:^{}}}'.format(note).format(item)
        result.append(temp)

    return result



print tower_builder(3)