import numpy as np

precos = np.array([100.0, 250.0, 300.0, 45.0])
print("Preços com desconto:", precos * 0.8)

matriz_vendas = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print("Matriz completa:\n", matriz_vendas)
print("Formato da matriz:", matriz_vendas.shape)

idadedes = np.array([15, 22, 17, 30, 45, 12, 18, 60])
print(idadedes[idadedes >= 18])
print(type(idadedes[idadedes >= 18]))

faturamento_diario = np.array([1200.50, 3400.00, 800.75, 4500.00, 2100.25])
print(f"Faturamento Total: R$ {faturamento_diario.sum()}")
print(f"Média Diária: R$ {faturamento_diario.mean()}")
print(f"Pior dia de vendas: R$ {faturamento_diario.min()}")
print(f"Melhor dia de vendas: R$ {faturamento_diario.max()}")