import math

x1 = int(input("Digite o primeiro número inteiro: "))
y1 = int(input("Digite o segundo número inteiro: "))
x2 = int(input("Digite o terceiro número inteiro: "))
y2 = int(input("Digite o terceiro número inteiro: "))

d = math.sqrt (((x2 - x1) ** 2 + (y2 - y1) ** 2))

if d >= 10:
	print("longe")
else:
	print("perto")