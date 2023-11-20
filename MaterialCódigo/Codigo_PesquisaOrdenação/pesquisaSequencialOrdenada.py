def ordered_sequential_search(a_list, item):
    i = 0
    found = False
    stop = False
    while i < len(a_list) and not found and not stop:
        if a_list[i] == item:
            found = True
        else:
            if a_list[i] > item:
                stop = True
            else:
                i = i + 1

    return found


test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(ordered_sequential_search(test_list, 3))
print(ordered_sequential_search(test_list, 13))
