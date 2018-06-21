def maior_elemento(lista):
	maior = lista[0]
	for i in range(len(lista)):
		if maior < lista[i]:
			maior = lista[i]
	return maior

lista = eval('[' + input("Digite sua lista: ") + ']')

print(maior_elemento(lista))