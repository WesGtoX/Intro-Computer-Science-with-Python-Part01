n = int(input("Digite um número inteiro: "))

i = 0
soma = 0

while i < n:
	a = n % 10
	n = n // 10
	soma = soma + a

print(soma)