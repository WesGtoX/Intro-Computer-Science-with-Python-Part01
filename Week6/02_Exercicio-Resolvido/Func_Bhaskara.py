import math

def delta(a, b, c):
    return (b **2) - (4 * a * c)

def main():
    a_dig = float(input("Digite o valor de a: "))
    b_dig = float(input("Digite o valor de b: "))
    c_dig = float(input("Digite o valor de c: "))
    imprime_raizes(a_dig, b_dig, c_dig)

def imprime_raizes(a, b, c):
    d = delta(a, b, c)
    if d == 0:
        x = (- b + math.sqrt(d)) / (2 * a)
        print("A única raiz é: ", x)
    else:
            if d < 0:
                print("Esta equação nao possui raizes reais")
            else:
                x1 = (- b + math.sqrt(d)) / (2 * a)
                x2 = (- b - math.sqrt(d)) / (2 * a)
                print("A primeira raiz é: ", x1)
                print("A segunda raiz é: ", x2)