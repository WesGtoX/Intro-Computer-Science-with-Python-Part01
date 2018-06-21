import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = (b ** 2) - (4 * a * c)

print(delta)

if (delta == 0):
	x = (-b + math.sqrt(delta)) / 2 * a
	print("A única raiz é:",x)

else:
	if (delta < 0):
		print("Esta equação não possui raizes reais!")
	else:
		x1 = (-b - math.sqrt(delta)) / 2 * a
		x2 = (-b + math.sqrt(delta)) / 2 * a
		print("A primeira raiz é: %d!\nA segunda raiz é: %d!" %(x1,x2))