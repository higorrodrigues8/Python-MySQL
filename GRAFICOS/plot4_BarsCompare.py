
import matplotlib.pyplot as plt

x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 5, 9]

x2 = [2, 4, 6, 8, 10]
y2 = [2, 3, 7, 5, 9]

titulo = "Grafico de barras"
legenda_x = "Eixo x"
legenda_y = "eixo y"
#_______________________TITULO
plt.title(titulo)
#_______________________
plt.bar(x1, y1, label = "grupo 1") #barras
plt.bar(x2, y2, label = "grupo 2") #barras
plt.legend()
#_______________________LEGENDAS
plt.xlabel(legenda_x)
plt.ylabel(legenda_y)
#_______________________
#_______________________SHOW
plt.show()
