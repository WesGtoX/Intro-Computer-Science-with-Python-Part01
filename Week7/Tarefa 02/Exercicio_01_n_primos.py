def éPrimo(x):
        fator = 2
        if x == 2:
                return True
        while x % fator != 0 and fator <= x/2:
            fator = fator + 1
        if x % fator == 0:
            return False
        else:
            return True

def n_primos(n):
	number = n
	i = 2
	primos = 0

	if n >= 2:
		while i <= n:
			if éPrimo(i):
				primos += 1
			i += 1	
	return primos