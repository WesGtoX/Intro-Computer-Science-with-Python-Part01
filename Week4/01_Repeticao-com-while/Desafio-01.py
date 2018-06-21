n = int(input("Digite um número inteiro: "))

soma = 0
while n > 0:
	i = n % 10
	n = n // 10
	soma = soma + i

print(soma)