from execut import Execution
from useful import Auxiliar
final = [1, 2, 3, 4, 5, 6, 7, 8, 0]

init = [2, 4, 3, 1, 0, 6, 7, 5, 8]

t = [2, 0, 3, 1 , 4, 6, 7, 5, 8]
aux = Auxiliar()
if (aux.verifReachable(init, final)):
	print "reachable"
	ex = Execution(init, final)
	ex.breadthSearchPrintProf()

else:
	print "not reachable"	
