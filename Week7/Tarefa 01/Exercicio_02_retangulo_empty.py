x = int(input("digite a largura: "))
y = int(input("digite a altura: "))

caractere = "#"

full_line = x * caractere
i = 0

if x > 2:
    empty = caractere + (" " * (x - 2)) + caractere
else:
    empty = full_line

if y >= 1:
    print(full_line)
for i in range(y - 2):
    print(empty)
if y >= 2:
    print(full_line)