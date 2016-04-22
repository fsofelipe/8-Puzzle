class Node(object):
	def __init__(self, state):
		self.parent = None
		self.state = state
		self.height = 0
		self.children = []

	def setNode(self, parent, height, children):	
		self.parent = parent
		self.height = height
		self.children = children
	
	def addChild(self, node):
		node.parent = self
		node.height = self.height + 1
		self.children.append(node)	
		
	def newStates(self, final):
		#print self.state
		if (self.height == 15): 
			print "max height"
			return False
		if (self.state == final): 
			print "I FOUND IT!"
			return True
		posZero = self.state.index(0)
		retorno = self.state[:]
		
		if posZero in [0,1,2,3,4,5]:	#Movimento para Baixo
			retorno[posZero], retorno[posZero+3] = retorno[posZero+3], retorno[posZero]
			if(self.checkLoop(retorno) == True): 
				#print "LOOP DOWN!"
				return False
			self.addChild(Node(retorno))
			num = len(self.children)
			for i in range(0, num-1):
				if(self.children[i].newStates(final)==True):
					return True
		retorno = self.state[:]
		
		if posZero in [3,4,5,6,7,8]:	#Movimento para Cima
			retorno[posZero], retorno[posZero-3] = retorno[posZero-3], retorno[posZero]
			if(self.checkLoop(retorno) == True): 
				#print "LOOP UP!"
				return False
			self.addChild(Node(retorno))
			num = len(self.children)
			for i in range(0, num-1):
				if(self.children[i].newStates(final)==True):
					return True
		retorno = self.state[:]
		
		if posZero in [0,1,3,4,6,7]:	#Movimento para Direita
			retorno[posZero], retorno[posZero+1] = retorno[posZero+1], retorno[posZero]
			if(self.checkLoop(retorno) == True): 
				#print "LOOP RIGHT!"
				return False
			self.addChild(Node(retorno))
			num = len(self.children)
			for i in range(0, num-1):
				if(self.children[i].newStates(final)==True):
					return True
		retorno = self.state[:]
		
		if posZero in [1,2,4,5,7,8]:	#Movimento para Esquerda
			retorno[posZero], retorno[posZero-1] = retorno[posZero-1], retorno[posZero]
			if(self.checkLoop(retorno) == True): 
				#print "LOOP LEFT!"
				return False
			self.addChild(Node(retorno))
			num = len(self.children)
			for i in range(0, num-1):
				if(self.children[i].newStates(final)==True):
					return True
		retorno = self.state[:]	
		

			
	def checkLoop(self, state):
		if(self.height == 0):
			return False
		elif(self.height-2 >= 0):
			if(self.parent.state == state):
				return True
		elif(self.height-4 >= 0):
			if(grampa(self.parent).state == state):
				return True
		elif(self.height-6 >= 0):
			if(grampa(grampa(self.parent)).state == state):
				return True
		elif(self.height-8 >= 0):
			if(grampa(grampa(grampa(self.parent))).state == state):
				return True
		else:
			return False
		
	def grampa(self):
		return self.parent.parent



