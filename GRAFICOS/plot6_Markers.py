
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 5, 9]

titulo = "Grafico de barras"
legenda_x = "Eixo x"
legenda_y = "eixo y"
#_______________________TITULO
plt.title(titulo)
#_______________________#scatter
plt.scatter(x, y, label="meus pontos", color="g", marker="o", s=100)
#_______________________#lines
plt.plot(x, y, color="k", linestyle="--")
#_______________________LEGENDAS
plt.xlabel(legenda_x)
plt.ylabel(legenda_y)
plt.legend()
#_______________________SHOW
plt.show()
