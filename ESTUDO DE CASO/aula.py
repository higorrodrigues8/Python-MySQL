entrada = open("16s_bacteria.fasta").read() #abre arquivo da bacteria e lê
saida = open("16s_bacteria.html","w") #cria um arquivo html

cont = {} #dicionario com combinações de proteinas e numeros
base = ['A', 'T', 'C', 'G'] #base de proteinas existentes

for i in base: #combina proteinas (todas as possibilidades)
	for j in base:
		cont[i+j] = 0 #combina e liga com um numero inteiro



entrada = entrada.replace("\n","") #substitui quebra de linha por continuação (nada)

for k in range(len(entrada)-1): #para k do tamanho da entrada menos um (pois é de par em par)
	cont[entrada[k]+entrada[k+1]] += 1 # CONTADOR RECEBE ENTRADA MAIS A POSIÇÃO DA FRENTE  E LIGA COM O NUMERO 1

# html
print(cont)
saida.write("<div>") #escreve no html de saida um div

i = 1
for k in cont: #percorre dicionario
	transparencia = cont[k]/max(cont.values()) #define o maior valor e divide todos por ele salvando o resultado na transfarencia

	saida.write("<div style='width:100px; border:1px solid #111; color:#fff; height:100px; float:left; background-color:rgba(0, 0, 0, "+str(transparencia)+"')>"+k+"</div>")
	#a transparencia do quadrado depende do resultado
	if i%4 == 0:
		saida.write("<div style='clear:both'></div>")

	i+=1

saida.close()
