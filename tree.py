class Node(object):
	def __init__(self, parent, state, height, children):	
		self.state = state
		self.children = []
	
	def addChild(self, node):
		self.children.append(node) 
		
		
	




