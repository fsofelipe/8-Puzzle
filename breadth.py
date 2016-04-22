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
		
	def alg (self, final):
		#Objeto Auxiliar
		aux = Auxiliar()

		#Listas
		nodeList = []
		visited = []


		#raiz da arvore
		raiz = Largura(self.state)
		raiz.setNode(None, 0, [])
		nodeList.append(raiz.state)
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
				nodeList.append(item)
		

		current = raiz.children[0]

		print raiz.state		

		while (len(nodeList) > 0):
			print current.state
			
			visited.append(current.state)

			if (current.state == final):
				break

			auxList = aux.newStates(current.state)
			#Cria novos estados para este nodo e adiciona para lista dos proximos nodos
			for item in auxList:
				try:
					check = visited.index(item)
				except:
					check = -1

				if (check == -1):
					#proximos nodos
					current.addChild(item)
					nodeList.append(item)
			print nodeList[0]
			del nodeList[0]

			if (len(nodeList) > 0):
				pai = current.parent
				for i in xrange (0, len(pai.children)):
					if (pai.children[i] == nodeList[0]):
						current = parent.children[i]
