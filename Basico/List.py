
minha_lista = [0, 10, 20, 30, 40, 50, 60]
print(minha_lista[2:5]) # 10, 20, 30
print(minha_lista[::-1]) # 60, 50, 40, 30, 20, 10, 0

dados_brutos = [1, 4, 7, 10, 13, 18, 21]
dados_pares = [numero for numero in dados_brutos if numero % 2 == 0] # honestamente pareceque que a unica utilidade disso é usar pouca linha. 
print(dados_pares) # 4, 10, 18
