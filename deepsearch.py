from useful import Auxiliar

class Profundidade(object):
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
		node = Profundidade(state)
		node.parent = self
		node.height = self.height + 1

		self.children.append(node)	
		
	def algorithm(self, final, maxheight):
		aux = Auxiliar()
		if(self.state == final):
			return self
		elif(self.height > maxheight):
			return False
		elif(self.checkLoop() == True):
			return False
		else:
			filhos = aux.newStates(self.state)
			for filho in filhos:
				self.addChild(filho)
			for x in self.children:
				state = x.algorithm(final, maxheight)
				if(state != False):
					return state
		if(self.height == 0):
			print "try higher maxheight"
		return False

	def getPrint(self, node):
		path = []
		if(node != False):
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


	def grampa(self):
			return self.parent.parent


	def checkLoop(self):
		if(self.height <= 1):
			return False
		elif(self.height-2 >= 0):
			if(self.grampa().state == self.state):
				return True
		elif(self.height-4 >= 0):
			if(grampa(grampa(self)).state == self.state):
				return True
		elif(self.height-6 >= 0):
			if(grampa(grampa(grampa(self))).state == self.state):
				return True
		elif(self.height-8 >= 0):
			if(grampa(grampa(grampa(grampa(self)))).state == self.state):
				return True
		else:
			return False
		
	