from collections import deque

fila_encadeada = deque([10, 20, 30])

fila_encadeada.appendleft(0)
fila_encadeada.append(40)
print(fila_encadeada)

fila_encadeada.rotate(2)
print(fila_encadeada)

fila_encadeada.rotate(-1)
print(fila_encadeada)
