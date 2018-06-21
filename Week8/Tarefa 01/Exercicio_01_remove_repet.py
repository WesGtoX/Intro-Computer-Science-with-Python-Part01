def remove_repetidos(lista):
	lista2 = []
	for i in lista:
		if i not in lista2:
			lista2.append(i)
	lista2.sort()
	return lista2

lista = eval('[' + input("Digite sua lista: ") + ']')

print(remove_repetidos(lista))