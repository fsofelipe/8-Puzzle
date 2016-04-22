from useful import Auxiliar
class Execution(object):
	def __init__ (self, initial, final):
		self.initial = initial
		self.final = final

	def breadthSearchList(self):
		lag = Largura(init)
		return lag.getPath(lag.algorithm(final))

	def breadthSearchPrint(self):
		path = breadthSearchList ()
		path.reverse()
		for i in path:
			print i
		