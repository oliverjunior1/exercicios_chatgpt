pedidos = [
    {"cliente": "Ana", "valor": 120.0, "itens": 3},
    {"cliente": "Bruno", "valor": 80.0, "itens": 1},
    {"cliente": "Carlos", "valor": 200.0, "itens": 5},
    {"cliente": "Ana", "valor": 50.0, "itens": 2},
    {"cliente": "Bruno", "valor": 300.0, "itens": 6},
]

# Calcule o valor total de todos os pedidos.
i = 0
total = 0
while i < len(pedidos):
    total += pedidos[i]['valor']
    i += 1
print(total)

# Use filter + lambda para retornar apenas pedidos com valor maior que 100.
pedidos_acima_100 = list(filter(lambda p: p["valor"] > 100, pedidos))
print(pedidos_acima_100)

# Use map para criar uma lista contendo apenas os valores dos pedidos.
valores_dos_pedidos = list(map(lambda a: a['valor'], pedidos))
print(valores_dos_pedidos)

# Crie um dicionário no formato:
# {
#     "Ana": 170.0,
#     "Bruno": 380.0,
#     "Carlos": 200.0
# }

gastos_por_cliente = {}

for p in pedidos:
    cliente = p['cliente']
    valor = p['valor']

    if cliente in gastos_por_cliente:
        gastos_por_cliente[cliente] += valor
    else:
        gastos_por_cliente[cliente] = valor

print(gastos_por_cliente)

# Descubra qual cliente gastou mais no total.
cliente_top = max(gastos_por_cliente, key=gastos_por_cliente.get)
print(cliente_top, gastos_por_cliente[cliente_top])


# Função reutilizável
def filtrar_por_valor(pedidos, minimo):
    return list(filter(lambda p: p["valor"] > minimo, pedidos))


print(filtrar_por_valor(pedidos, 150))

# EXTRA: Ticket médio por cliente
ticket_medio = {}

contagem = {}

for p in pedidos:
    cliente = p['cliente']
    valor = p['valor']

    if cliente in ticket_medio:
        ticket_medio[cliente] += valor
        contagem[cliente] += 1
    else:
        ticket_medio[cliente] = valor
        contagem[cliente] = 1

for cliente in ticket_medio:
    ticket_medio[cliente] = ticket_medio[cliente] / contagem[cliente]

print(ticket_medio)

# EXTRA: Ordenar pedidos do maior para o menor valor
pedidos_ordenados = sorted(pedidos, key=lambda p: p["valor"], reverse=True)
print(pedidos_ordenados)