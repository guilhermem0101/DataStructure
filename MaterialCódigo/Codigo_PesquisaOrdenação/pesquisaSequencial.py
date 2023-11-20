def sequential_search(lista, item):
    i = 0
    found = False
    #Enquanto i é menor que o tamanho da lista
    while i < len(lista) and not found:
        if lista[i] == item:
            found = True
        else:
             i = i + 1

    return found


test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequential_search(test_list, 3))
print(sequential_search(test_list, 13))
