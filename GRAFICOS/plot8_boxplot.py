
import matplotlib.pyplot as plt
import random

vetor = [1,323,2,323,21,35,6,767,76,34,45]
for i in range(10):
    numero_aleatorio = random.randint(0,1)
    vetor.append(numero_aleatorio)

plt.title("boxplot")
plt.boxplot(vetor)
plt.show()
