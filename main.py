import tkMessageBox
from Tkinter import *
from execut import Execution
from useful import Auxiliar



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

def outputMoves(outputList):	#Printa os elementos da lista 3 a 3 e quebra 1 linha
	output.insert(END, "Numero de passos: " + str(len(outputList)-1))
	output.insert(END,"\n\n")
	for i in outputList:
		for j in range(0,9,3):
			show = str(i[j]) + " " + str(i[j+1]) + " " + str(i[j+2])
			output.insert(END, show)
			output.insert(END,"\n")

		output.insert(END,"\n")

def checkHeight():              #valida a altura
        if (heightEntry.get() == ""):
                h = 25
                output.insert(END, "Altura padrao: 25\n")
        else:
                h = int(heightEntry.get())
                if h >= 60:
                        h = 60
                        output.insert(END, "Altura muito grande, vamos deixar em 60\n")
                elif h <= 0:
                        h = 25
                        output.insert(END, "Altura negativa? kkkk, vamos deixar em 25\n")
        return h
        


def runSearch(): 		#executa tudo
	erro = checkStages()
	if (erro == False):
		inicial = makeStage(inicialEntry.get())
		final = makeStage(finalEntry.get())
		aux = Auxiliar()
		output.delete(1.0, END)

		if (aux.verifReachable(inicial, final)):

			output.insert(END,"Estado Alcancavel\n")

			ex = Execution(inicial, final)
			outputList = []
			if(int(v.get() == 1)):
				height = checkHeight()
				outputList = ex.deeperSearchList(height)
				outputMoves(outputList)
				
			else:
				heightEntry.delete(0, END)
				outputList = ex.breadthSearchList()
				outputMoves(outputList)
		else:

				output.insert(END,"Estado NAO Alcancavel\n")


##############################################################



## !!!!!!!!!!!!!!! INTERFACE !!!!!!!!!!! START !!!!!!!!!!!!! ##


root = Tk()
root.title("Trabalho de FIA")


################ ENTRADAS ###########################
labelInicial = Label(root, text="Estagio Inicial ")
labelFinal = Label(root, text="Estagio Final ")
labelHeight = Label(root, text="Altura Maxima ")
inicialEntry = Entry(root)
finalEntry = Entry(root)
heightEntry = Entry(root)
labelInicial.grid(row=0, column=0, pady=5)
inicialEntry.grid(row=0, column=1, pady=5, padx=7)
labelFinal.grid(row=1, column=0, pady=5)
finalEntry.grid(row=1, column=1, pady=5, padx=7)
labelHeight.grid(row=3, column=0, pady=5)
heightEntry.grid(row=3, column=1, pady=5, padx=7)

################ ALGORITMO ##########################
v = IntVar()
v.set(1)
Radiobutton(root, text="Busca em Profundidade", variable=v, value=1).grid(row=2, column=0)
Radiobutton(root, text="Busca em Largura", variable=v, value=2).grid(row=2, column=1)

############ RODA O PROGRAMA ########################
buttonSearch = Button(root, text="Buscar", command=runSearch)
buttonSearch.grid(row=4, column=0, pady=5)

############ LIMPA ENTRADAS ######################
buttonClear = Button(root, text="Limpar", command=clear)
buttonClear.grid(row=4, column=1, pady=5)

############# EXIBE SAIDA ##########################
output = Text(root, width=22, height=8)
output.grid(row=5, column=0, columnspan=2, pady=10)

####################################################

root.mainloop()
