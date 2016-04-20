from useful import Auxiliar
from tree import Node

init = [1, 2, 3, 4, 0, 6, 7, 5, 8]

final = [1, 2, 3, 4, 5, 6, 7, 8, 0]


tree = Node(init)
tree.newStates(final)

#print "INITIAL STATE:"
#initialState = Aux.createState()
#print ""
#print "FINAL STATE:"
#finalState = Aux.createState()

#print "INITIAL STATE:"
#print initialState
#print "FINAL STATE:"
#print finalState

#Aux.verifReachable(initialState, finalState)
#Aux.verifReachable(stateA, stateB)
#Aux.newStates(stateA)

#arvore = Node(stateD)
#arv = Node(stateB)
#arv2 = Node(stateC)
#arv3 = Node(stateA)

#arvore.addChild(arv)
#arv.addChild(arv3)
#arv3.addChild(arvore)
#print arvore.state
#print arvore.children[1].state

#Aux.newStates(stateA)

