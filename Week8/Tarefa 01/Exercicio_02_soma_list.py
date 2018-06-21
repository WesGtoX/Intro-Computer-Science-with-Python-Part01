def soma_elementos(lista):
        soma = 0
        for i in lista:
                soma = soma + i
        return soma

lista = eval('[' + input("Digite sua lista: ") + ']')

print(soma_elementos(lista))