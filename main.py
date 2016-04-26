import tkMessageBox
from Tkinter import *
from execut import Execution
from useful import Auxiliar


<<<<<<< HEAD
=======
t = [2, 0, 3, 1 , 4, 6, 7, 5, 8]
aux = Auxiliar()
if (aux.verifReachable(init, final)):
	print "reachable"
	ex = Execution(init, final)
	print " "
	print "Widht Search"
	ex.breadthSearchPrint()
	print "Deep Search"
	ex.deeperSearchPrint(15)
>>>>>>> d4e0402ed171b738fb1560793fe7561255c568a0

############### METODOS PARA INTERFACE #######################


def clear():			#Limpa os campos
	inicialEntry.delete(0, END)
	finalEntry.delete(0, END)
	output.delete(1.0, END)

def checkStages():		#Checa se as entradas estao corretas
	checkInicial = inicialEntry.get()
	checkFinal = finalEntry.get()
	erro = True if (len(checkInicial) != 9) or (len(checkFinal) != 9) else False
	if(erro == True):
		tkMessageBox.showinfo("Erro", "Os campos devem ter 9 numeros")
	else:
		return False

def makeStage(stage):	#Cria listas de ints com as entradas
	newStage = []
	for i in range(0, 9):
		newStage.append(int(stage[i]))
	return newStage

def outputMoves():
	output.insert(END, "teste")

def runSearch(): 		#executa tudo
	erro = checkStages()
	if (erro == False):
		inicial = makeStage(inicialEntry.get())
		final = makeStage(finalEntry.get())
		aux = Auxiliar()
		
		if (aux.verifReachable(inicial, final)):
			print "reachable"
			ex = Execution(inicial, final)

			if(int(v.get() == 1)):
				ex.deeperSearchPrint(15)
				outputMoves()
			else:
				ex.breadthSearchPrint()
				outputMoves()
		else:
				print "not reachable"
		

##############################################################



## !!!!!!!!!!!!!!! INTERFACE !!!!!!!!!!! START !!!!!!!!!!!!! ##


root = Tk()
root.title("Trabalho de FIA")


################ ENTRADAS ###########################
labelInicial = Label(root, text="Estagio Inicial ")
labelFinal = Label(root, text="Estagio Final ")
inicialEntry = Entry(root)
finalEntry = Entry(root)
labelInicial.grid(row=0, column=0, pady=5)
inicialEntry.grid(row=0, column=1, pady=5, padx=7)
labelFinal.grid(row=1, column=0, pady=5)
finalEntry.grid(row=1, column=1, pady=5, padx=7)

################ ALGORITMO ##########################
v = IntVar()
v.set(1)
Radiobutton(root, text="Busca em Profundidade", variable=v, value=1).grid(row=2, column=0)
Radiobutton(root, text="Busca em Largura", variable=v, value=2).grid(row=2, column=1)

############ RODA O PROGRAMA ########################
buttonSearch = Button(root, text="Buscar", command=runSearch)
buttonSearch.grid(row=3, column=0, pady=5)

############ LIMPA ENTRADAS ######################
buttonClear = Button(root, text="Limpar", command=clear)
buttonClear.grid(row=3, column=1, pady=5)

############# EXIBE SAIDA ##########################
output = Text(root, width=33, height=8)
output.grid(row=4, column=0, columnspan=2, pady=10)

####################################################

root.mainloop()