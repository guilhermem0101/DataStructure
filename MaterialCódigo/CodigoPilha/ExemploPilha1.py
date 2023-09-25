from Stack import Stack
# criar objeto do tipo Pilha


def verifica_palindromo(e_string):
    obj_pilha = Stack()
    for caracter in e_string:
        obj_pilha.push(caracter)

    f_string = ""
    while not obj_pilha.is_empty():
        f_string = f_string + str(obj_pilha.pop())

    if e_string == f_string:
        return "Entrada de dados forma um palíndromo"

    return "Entrada de dados nao forma um palíndromo"
print(verifica_palindromo("lsdkjfskf"))

