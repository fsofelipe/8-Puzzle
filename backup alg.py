	def alg (self, final):
		#lista com os estados de fronteira
		#armazena estados e nao nodos
		nodeList = [] 
		nodeList.append (self)


		visited = []

		aux = Auxiliar()

		curent = nodeList[0]

		while (len(nodeList) > 0 ):
			print current
			
			visited.append(current)

			if (current == final):
				break
			auxList = aux.newStates(current)
			
			for item in auxList:
				try: 
					check = visited.index(item)
				except:
					check = -1
				
				if (check == -1): 
					#proximos nodos
					nd = Largura(item)

					nodeList.append(nd)
				

			del nodeList[0]

			if len(nodeList) > 0:
				current = nodeList[0]