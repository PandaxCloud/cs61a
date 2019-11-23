def even_weighted(lst):
    return [lst[index] * index for index in range(len(lst)) if index % 2 == 0]

def max_product(lst):
    if not lst:
        return 1
    elif len(lst) == 1:
        return lst[0]
    else:
        # return max(lst[0] * max_product(lst[2:]), lst[1] * max_product(lst[3:]))
        lst1 = lst[:]
        del lst1[0:2]
        result1 = lst[0] * max_product(lst1)
        lst2 = lst[:]
        del lst2[0:3]
        result2 = lst[1] * max_product(lst2)
        return max(result1, result2)

def max_product2(lst):
    if lst == []:
        return 1
    # elif len(lst) == 1:
    #     return lst[0]
    else:
        return max(max_product(lst[1:]), lst[0]*max_product(lst[2:]))

def mario_number(level):
    if len(level) < 3:
        return 1
    else:
        if level[1] == 'P':
            if level[2] == 'P':
                return 0
            else:
                return mario_number(level[2:])
        else:
            if level[2] == 'P':
                return mario_number(level[1:])
            else:
                return mario_number(level[2:]) + mario_number(level[1:])

