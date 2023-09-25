#LIFO
class Stack:
    def __init__(self): # Inicia uma instancia da classe lista
        self.items = []

    def is_empty(self): # Retorna True ou False, condição da lista estar ou não vazia
        return self.items == [] 

    def push(self, item): # Adiciona ao final
        self.items.append(item) 

    def pop(self): # Adiciona no final
        return self.items.pop()

    def peek(self): # Retorna o ultimo item
        return self.items[len(self.items) - 1]

    def size(self): # Retorna o tamanho
        return len(self.items)

    def imprimir(self): #imprime a pilha
        i = len(self.items) - 1
        while i >= 0:
            print("|", self.items[i])
            i = i - 1
