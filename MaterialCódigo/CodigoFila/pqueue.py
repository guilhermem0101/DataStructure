class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item, priority):
        # Adiciona um elemento com sua prioridade
        self.items.insert(0, (item, priority))

    def dequeue(self):
        if not self.is_empty():
            max_priority_item = max(self.items, key=lambda x: x[1])
            self.items.remove(max_priority_item)
            return max_priority_item[0]

    def size(self):
        return len(self.items)

# Exemplo de uso
pq = PriorityQueue()
pq.enqueue("Tarefa 1", 3)  # Tarefa 1 com prioridade 3
pq.enqueue("Tarefa 2", 1)  # Tarefa 2 com prioridade 1
pq.enqueue("Tarefa 3", 2)  # Tarefa 3 com prioridade 2

while not pq.is_empty():
    print("Executando:", pq.dequeue())
