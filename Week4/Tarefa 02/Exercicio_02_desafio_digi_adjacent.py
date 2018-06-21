n = int(input("Digite um número inteiro: "))

a = n % 10
n = n // 10
adj = False

while n > 0 and not adj:
        x = n % 10
        if x == a:
                adj = True
        a = x
        n = n // 10
if adj:
        print("sim")
else:
        print("não")
