
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 5, 9]
tamanho_marcador = [20, 5, 100, 33, 10]
titulo = "Grafico de barras"
legenda_x = "Eixo x"
legenda_y = "eixo y"
#_______________________TITULO
plt.title(titulo)
#_______________________#scatter
plt.scatter(x, y, label="meus pontos", color="000000", marker="o", s=tamanho_marcador)
#_______________________#lines
plt.plot(x, y, color="#990000", linestyle="-")
#_______________________LEGENDAS
plt.xlabel(legenda_x)
plt.ylabel(legenda_y)
plt.legend()
#_______________________SHOW
#plt.show()
#_______________________SAVE
plt.savefig("exemplo.png", dpi=1200)
