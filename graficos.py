import matplotlib.pyplot as plt

# Dados do gráfico de barra, linha e Scatterplot
x = [1, 2, 3, 4]
y = [2, 6, 4, 1]

# Dados para comparar gráficos
x1 = [1, 3, 5, 7, 9]
y1 = [3, 6, 7, 20, 4]

x2 = [2, 4, 6, 8, 10]
y2 = [7, 3, 8, 1, 11]

titulo = 'Gráfico de linha simples'
eixox = 'Dias'
eixoy = 'Horas estudadas'

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

# Gerando gráfico de barra
'''plt.bar(x, y)
plt.show()'''

# Gerando gráfico de linha
'''plt.plot(x, y)
plt.show()'''

# Comparar os gráficos
'''plt.bar(x1, y1, label='Grupo 1')
plt.plot(x2, y2, label='Grupo 2')
plt.legend()
plt.show()'''

# Gerando gráfico de dispersão sem linhas
'''plt.scatter(x, y, label='Notas')
plt.legend()
plt.show()'''

# Gerando gráfico de dispersão com linhas
'''plt.scatter(x, y, label='Notas', color='red', marker='*', s=100)
plt.plot(x, y)
plt.legend()
plt.show()'''

# Documentação oficial do matplotlib
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
