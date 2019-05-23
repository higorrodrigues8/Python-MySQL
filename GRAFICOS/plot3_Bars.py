
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 5, 9]

titulo = "Grafico de barras"
legenda_x = "Eixo x"
legenda_y = "eixo y"
#_______________________TITULO
plt.title(titulo)
#_______________________
plt.bar(x, y) #barras
#_______________________LEGENDAS
plt.xlabel(legenda_x)
plt.ylabel(legenda_y)
#_______________________
#_______________________SHOW
plt.show()
