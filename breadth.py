from useful import Auxiliar
class Largura(object):
	def __init__(self, state):
		self.parent = None
		self.state = state
		self.height = 0
		self.children = []

	def setNode(self, parent, height, children):	
		self.parent = parent
		self.height = height
		self.children = children
	
	def addChild(self, state):
		node = Largura(state)
		node.parent = self
		node.height = self.height + 1

		self.children.append(node)	
		
	def algorithm(self, final):
		#Objeto Auxiliar
		aux = Auxiliar()

		#Listas
		visited = []
		irmaos = []
		proximos = []

		#raiz da arvore
		raiz = Largura(self.state)
		raiz.setNode(None, 0, [])

		auxList = aux.newStates(raiz.state)

		visited.append(raiz.state)

		for item in auxList:
			try:
				check = visited.index(item)
			except:
				check = -1

			if (check == -1):
				#proximos nodos
				raiz.addChild(item)

		irmaos = raiz.children

		sai = False
		while (len(irmaos) != 0 and sai == False):
			for current in irmaos:
				
				if (current.state == final):
					sai = True
					break
				#Gera novos estados
				auxList = aux.newStates(current.state)
			
				for item in auxList:
					try: 
						check = visited.index(item)
					except:
						check = -1
				
					if (check == -1): 
						#proximos nodos
						current.addChild(item)
						visited.append(item)

						if (len(current.children) > 0):
							filho = len(current.children) - 1
						else:
						 	filho = 0
						
						proximos.append(current.children[filho])

				irmaos.remove(current)
			
			irmaos = proximos

			#print current.state

		return current

	def getPrint(self, node):
		path = []
		while(node.parent != None):
			path.append(node.state)
			node = node.parent
		path.append(node.state)

		path.reverse()

		for i in path:
			print i

	def getList(self, node):
		path = []
		while(node.parent != None):
			path.append(node.state)
			node = node.parent
		path.append(node.state)

		path.reverse()

		return path