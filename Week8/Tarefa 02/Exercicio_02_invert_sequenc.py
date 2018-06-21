number = []

while True:
	i = int(input("Digite um número: "))
	if i == 0:
		break
	else:
		number.append(i)
		
for n in number[::-1]:
	print(n)