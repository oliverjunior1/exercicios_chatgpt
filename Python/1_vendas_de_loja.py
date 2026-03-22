pedidos = [
    {"cliente": "Ana", "valor": 120.0, "itens": 3},
    {"cliente": "Bruno", "valor": 80.0, "itens": 1},
    {"cliente": "Carlos", "valor": 200.0, "itens": 5},
    {"cliente": "Ana", "valor": 50.0, "itens": 2},
    {"cliente": "Bruno", "valor": 300.0, "itens": 6},
]

# Calcule o valor total de todos os pedidos.
i = 0
sum = 0
while i<len(pedidos):
    sum += pedidos[i]['valor']
    i+= 1
print(sum)

# Use filter + lambda para retornar apenas pedidos com valor maior que 100.
# maior_que_100 = filter(lambda pe)

