def MinMax(temperaturas):
	print("A menor temperatura do mês foi: ", minima(temperaturas), "C.")
	print("A maior temperatura do mês foi: ", maxima(temperaturas), "C.")

def maxima(temps):
	max = temps[0]
	i = 1
	while i < len(temps):
		if temps[i] > max:
			max = temps[i]
		i += 1
	return max

def minima(temps):
	min = temps[0]
	i = 1
	while i < len(temps):
		if temps[i] < min:
			min = temps[i]
		i += 1
	return min

# ---------------------------------------------
# --------- TESTES AUTOMATIZAADOS MAX ---------
# ---------------------------------------------

def teste_pontual_max(temp,valor_esperado):
	valor_calculado = maxima(temp)
	if valor_calculado != valor_esperado:
		print("Valor errado para array: ", temp)
		print("Valor esperado: %d. Valor calculado: %d" %(valor_esperado,valor_calculado))

def testa_maxima():
	print("Iniciando os testes")
	print("---------------------\n")

	i = 0
	lista = [[0,1],[0,0,0,5,0,0,],[0,1,2,3,4,5,6,7,8,9,10],[30,27,25,26,29,31,32,33,30,29,24,26,30,27,24,25,26,24,22,23,25,25,28,28,32,32,31,29,28,31,33],[-15,-12,-20,-30]]
	val = [1,5,10,33,-12]
	for i in range(len(lista)):
		teste_pontual_max(lista[i],val[i])

	print("\n---------------------")
	print("Finalizando os testes")

# ---------------------------------------------
# --------- TESTES AUTOMATIZAADOS MIN ---------
# ---------------------------------------------

def teste_pontual_min(temp,valor_esperado):
	valor_calculado = minima(temp)
	if valor_calculado != valor_esperado:
		print("Valor errado para array: ", temp)
		print("Valor esperado: %d. Valor calculado: %d" %(valor_esperado,valor_calculado))

def testa_minima():
	print("Iniciando os testes")
	print("---------------------\n")
	
	i = 0
	lista = [[0],[0,0,0,0,0,0,],[0,1,2,3,4,5,6,7,8,9,10],[30,27,25,26,29,31,32,33,30,29,24,26,30,27,24,25,26,24,22,23,25,25,28,28,32,32,31,29,28,31,33],[-15,-12,0,20,30]]
	val = [0,0,0,22,-15]
	for i in range(len(lista)):
		teste_pontual_min(lista[i],val[i])

	print("\n---------------------")
	print("Finalizando os testes")