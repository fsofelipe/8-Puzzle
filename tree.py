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
		
		
	




