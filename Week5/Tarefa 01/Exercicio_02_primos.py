def ePrimo(k):
    primo = True
    divisor = 2
    while divisor < k and primo:
        if k % divisor == 0:
            primo = False
        divisor += 1
    if primo and k != 1:
        return True
    else:
        return False

def maior_primo(k):
    maior = 2
    i = 2
    while i <= k:
        if ePrimo(i):
            maior = i
        i += 1
    return maior