import matplotlib.pylab as plt

# Crie um gráfico de linha usando o Matplotlib que:

meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]
vendas = [1500, 1800, 1700, 2000, 2200, 2100]

# Mostre os meses no eixo X
# Mostre as vendas no eixo Y
# Mostre marcadores nos pontos da linha
plt.plot(meses, vendas, marker='o')

# Tenha rótulos nos eixos:
# X → "Meses"
# Y → "Vendas (R$)"

plt.xlabel("Meses")
plt.ylabel("Vendas (R$)")


# Tenha um título: "Vendas no 1º Semestre"
plt.title("Vendas no 1º Semestre")

# Exiba o gráfico na tela
plt.show()




