from useful import Auxiliar

stateB = list(range (9))
stateB[0] = 1
stateB[1] = 2
stateB[2] = 3
stateB[3] = 4
stateB[4] = 5
stateB[5] = 6
stateB[6] = 7
stateB[7] = 8
stateB[8] = 0

stateA = list(range(9))
stateA[0] = 2
stateA[1] = 4
stateA[2] = 3
stateA[3] = 1
stateA[4] = 0
stateA[5] = 6
stateA[6] = 7
stateA[7] = 5
stateA[8] = 8

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

Aux.verifReachable(stateA, stateB)
Aux.newStates(stateA)
