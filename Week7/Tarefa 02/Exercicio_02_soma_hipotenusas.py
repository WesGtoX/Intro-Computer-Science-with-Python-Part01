def calc_hip(a,b):
	return ((a * a) + (b * b))

def soma_hipotenusas(n):
	i = 1
	sum = 0
	while i <= n:
		ca = (i * i)
		a = 1
		b = 1
		while a < n:
			while b < n:
				if ca == calc_hip(a,b):
					sum += i
					a = n
					break
				b += 1
			a += 1
			b = a
		i += 1
	return sum