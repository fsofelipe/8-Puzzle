from useful import Auxiliar
from tree import Node
stateB = [1, 2, 3, 4, 5, 6, 7, 8, 0]

stateA = [2, 4, 3, 1, 0, 6, 7, 5, 8]

stateC = [8, 7, 6, 5, 4, 3, 2, 1, 0]
Aux = Auxiliar()
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

arvore = Node(stateA)
arv = Node(stateB)
arv2 = Node(stateC)

arvore.addChild(arv)
arvore.addChild(arv2)
#print arvore.state
#print arvore.children[1].state

Aux.newStates(stateB)

