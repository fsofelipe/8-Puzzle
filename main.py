from useful import Auxiliar
finalState = list(range (9))
#finalState[0] = 2
#finalState[1] = 4
#finalState[2] = 3
#finalState[3] = 1
#finalState[4] = 0
#finalState[5] = 6
#finalState[6] = 7
#finalState[7] = 5
#finalState[8] = 8

#finalState[0] = 1
#finalState[1] = 2
#finalState[2] = 3
#finalState[3] = 4
#finalState[4] = 5
#finalState[5] = 6
#finalState[6] = 7
#finalState[7] = 8
#finalState[8] = 0

initialState = list(range(9))
initialState[0] = 0
initialState[1] = 1
initialState[2] = 4
initialState[3] = 2
initialState[4] = 5
initialState[5] = 3
initialState[6] = 8
initialState[7] = 7
initialState[8] = 6

#initialState[0] = 8
#initialState[1] = 7
#initialState[2] = 6
#initialState[3] = 5
#initialState[4] = 4
#initialState[5] = 3
#initialState[6] = 2
#initialState[7] = 1
#initialState[8] = 0


Aux = Auxiliar()

Aux.verifReachable(initialState, finalState)
#teste = []
#teste = Aux.createState()
initialState = Aux.createState()
Aux.verifReachable(initialState, finalState)
print initialState
