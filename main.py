from useful import Auxiliar
from tree import Node
from breadth import Largura
final = [1, 2, 3, 4, 5, 6, 7, 8, 0]

init = [2, 4, 3, 1, 0, 6, 7, 5, 8]

t = [2, 0, 3, 1 , 4, 6, 7, 5, 8]

aux = Auxiliar()

if (aux.verifReachable(init, final)):
	print "reachable"

	teste = Largura(init)

	teste.printParent(teste.alg(final))


else:
	print "not reachable"	
