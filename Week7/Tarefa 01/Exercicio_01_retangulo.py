x = int(input("digite a largura: "))
y = int(input("digite a altura: "))

z = x
while y > 0:
	while x > 0:
		print("#", end = "")
		x = x - 1
	x = z
	print()
	y = y - 1