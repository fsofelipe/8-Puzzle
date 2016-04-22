class Auxiliar():
	def createState(self):
		state = []
		for x in xrange(0, 9):
			state.append = input("Informe o " + str(x+1) +"o valor para o estado: ")
		return state
		
	def verifReachable(self, initial, final):
		inv = 0
		
		for posInit in xrange(0, 9): #vetor inicial
			
			if (initial[posInit] != 0):
				
				posFinal = final.index(initial[posInit])
				aux=[] #cria uma lista com todos os elementos que podem ocorrer antes do atual
				for x in xrange(0, posFinal):
					if (final[x] != 0):
						aux.append(final[x])
				#print str(initial[posInit]) 
				#print aux
				for i in xrange (posInit, 9):
					for j in xrange (0, len(aux)):
						if (initial[i] == aux[j]):
							#print "inversao"
							inv = inv + 1
		#print inv		
		if (inv % 2) == 0:	
			return True
		else:
			return False

	def newStates(self, state):
		posZero = state.index(0)
		estado = state[:]
		retorno = []
		if posZero in [0,1,2,3,4,5]:	#Movimento para Baixo
			estado[posZero], estado[posZero+3] = estado[posZero+3], estado[posZero]
			retorno.append(estado)
			estado = state[:]

		if posZero in [3,4,5,6,7,8]:	#Movimento para Cima
			estado[posZero], estado[posZero-3] = estado[posZero-3], estado[posZero]
			retorno.append(estado)
			estado = state[:]
		
		if posZero in [0,1,3,4,6,7]:	#Movimento para Direita
			estado[posZero], estado[posZero+1] = estado[posZero+1], estado[posZero]
			retorno.append(estado)
			estado = state[:]

		if posZero in [1,2,4,5,7,8]:	#Movimento para Esquerda
			estado[posZero], estado[posZero-1] = estado[posZero-1], estado[posZero]
			retorno.append(estado)
			estado = state[:]

		return retorno
	
		
		
	
