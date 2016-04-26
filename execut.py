from breadth import Largura
from deepsearch import Profundidade
class Execution(object):
	def __init__ (self, init, meta):
		self.initial = init
		self.final = meta

	def breadthSearchList(self):
		lag = Largura(self.initial)
		return lag.getList(lag.algorithm(self.final))

	def breadthSearchPrint(self):
		lag = Largura(self.initial)
		return lag.getPrint(lag.algorithm(self.final))

	def deeperSearchPrint(self, maxheight):
		prof = Profundidade(self.initial)
		return prof.getPrint(prof.algorithm(self.final, maxheight))

	def deeperSearchList(self, maxheight):
		prof = Profundidade(self.initial)
		return prof.getList(prof.algorithm(self.final, maxheight))