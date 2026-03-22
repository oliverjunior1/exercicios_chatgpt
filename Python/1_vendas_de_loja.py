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
pedidos_acima_100 = list(filter(lambda p: p["valor"] > 100, pedidos))

print(pedidos_acima_100)

# Use map para criar uma lista contendo apenas os valores dos pedidos.
valores_dos_pedidos = list(map(lambda a: a['valor'],pedidos))
print(valores_dos_pedidos)

# Crie um dicionário no formato:{
#     "Ana": 170.0,
#     "Bruno": 380.0,
#     "Carlos": 200.0
# }
my_dict = {a['cliente']:a['valor'] for a in pedidos}
print(my_dict)

# Descubra qual cliente gastou mais no total.
for x,y in zip(my_dict):
    print(x)



