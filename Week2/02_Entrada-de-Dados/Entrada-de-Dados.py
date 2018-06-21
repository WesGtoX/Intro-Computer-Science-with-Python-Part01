Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
======== RESTART: F:\CURSOS\CCPython\Week2\ConversorDeTemperatura.py ========
Traceback (most recent call last):
  File "F:\CURSOS\CCPython\Week2\ConversorDeTemperatura.py", line 3, in <module>
    temperaturaCelsius = (F - 23) * 5 / 9
NameError: name 'F' is not defined
>>> 
======== RESTART: F:\CURSOS\CCPython\Week2\ConversorDeTemperatura.py ========
Traceback (most recent call last):
  File "F:\CURSOS\CCPython\Week2\ConversorDeTemperatura.py", line 3, in <module>
    temperaturaCelsius = (F - 23) * 5 / 9
NameError: name 'F' is not defined
>>> 
======== RESTART: F:\CURSOS\CCPython\Week2\ConversorDeTemperatura.py ========
A temperatura em celsius é 30.555555555555557
>>> 
======== RESTART: F:\CURSOS\CCPython\Week2\ConversorDeTemperatura.py ========
A temperatura em celsius é 25.555555555555557
>>> 
======== RESTART: F:\CURSOS\CCPython\Week2\ConversorDeTemperatura.py ========
A temperatura em celsius é -6.666666666666667
>>> 
======== RESTART: F:\CURSOS\CCPython\Week2\ConversorDeTemperatura.py ========
Digite uma temperatura em Fahrenheit 20
Traceback (most recent call last):
  File "F:\CURSOS\CCPython\Week2\ConversorDeTemperatura.py", line 3, in <module>
    temperaturaCelsius = (temperaturaFahrenheit - 32) * 5 / 9
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> 
======== RESTART: F:\CURSOS\CCPython\Week2\ConversorDeTemperatura.py ========
Digite uma temperatura em Fahrenheit 34
A temperatura em celsius é 1.1111111111111112
>>> 
======== RESTART: F:\CURSOS\CCPython\Week2\ConversorDeTemperatura.py ========
Digite uma temperatura em Fahrenheit: 200
A temperatura em celsius é 93.33333333333333
>>> 
======== RESTART: F:\CURSOS\CCPython\Week2\ConversorDeTemperatura.py ========
Digite uma temperatura em Fahrenheit: 200
A temperatura em celsius é 93.33333333333333
>>> 
>>> 
>>> 
================ RESTART: F:\CURSOS\CCPython\Week2\Educado.py ================
Qual o nome da sua mãe?
================ RESTART: F:\CURSOS\CCPython\Week2\Educado.py ================
Qual o nome da sua mãe? Eliesana
Qual o nome do seu pai? José Mendes
Traceback (most recent call last):
  File "F:\CURSOS\CCPython\Week2\Educado.py", line 4, in <module>
    print("Bom dia Sra.", nomeDaMãe," E bom dia Sr. ", nomeDoPai)
NameError: name 'nomeDaMãe' is not defined
>>> 
================ RESTART: F:\CURSOS\CCPython\Week2\Educado.py ================
Qual o nome da sua mãe? Eliesana
Qual o nome do seu pai? José Mendes
Bom dia Sra. Eliesana  E bom dia Sr.  José Mendes
>>> 
================ RESTART: F:\CURSOS\CCPython\Week2\Educado.py ================
Qual o nome da sua mãe? Eliesana
Qual o nome do seu pai? José Mendes
Bom dia Sra. Eliesana !!! E bom dia Sr.  José Mendes
>>> 
================ RESTART: F:\CURSOS\CCPython\Week2\Educado.py ================
Qual o nome da sua mãe? Eliesana
Qual o nome do seu pai? José Mendes
Bom dia Sra. Eliesana !!! E bom dia Sr. José Mendes
>>> 
================ RESTART: F:\CURSOS\CCPython\Week2\Educado.py ================
Qual o nome da sua mãe? Eliesana
Qual o nome do seu pai? José Mendes
Bom dia Sra. Eliesana !!! E bom dia Sr. José Mendes .
>>> 
================ RESTART: F:\CURSOS\CCPython\Week2\Educado.py ================
Qual o nome da sua mãe? Eliesana
Qual o nome do seu pai? José Mendes
Bom dia Sra. Eliesana !!! E bom dia Sr. José Mendes .
>>> 
============= RESTART: F:\CURSOS\CCPython\Week2\ContaSegundos.py =============
Traceback (most recent call last):
  File "F:\CURSOS\CCPython\Week2\ContaSegundos.py", line 1, in <module>
    segundos_str - input("Por favor, entre com o número de segundos que deseja converter: ")
NameError: name 'segundos_str' is not defined
>>> 
============= RESTART: F:\CURSOS\CCPython\Week2\ContaSegundos.py =============
Por favor, entre com o número de segundos que deseja converter: 58000
Traceback (most recent call last):
  File "F:\CURSOS\CCPython\Week2\ContaSegundos.py", line 9, in <module>
    print(horas, "horas, ", munutos, "minutos e", segs_restantes_final, "segundos.")
NameError: name 'munutos' is not defined
>>> 
============= RESTART: F:\CURSOS\CCPython\Week2\ContaSegundos.py =============
Por favor, entre com o número de segundos que deseja converter: 58000
16 horas,  6 minutos e 40 segundos.
>>> 58000 // 3600
16
>>> 58000 % 3600
400
>>> 400 // 60
6
>>> 400 % 60
40
>>> 40 % 60
40
>>> 
>>> 
>>> 
>>> str
<class 'str'>
>>> Exercicio
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    Exercicio
NameError: name 'Exercicio' is not defined
>>> Exercicio = str
>>> str
<class 'str'>
>>> exercicio
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    exercicio
NameError: name 'exercicio' is not defined
>>> "Exercicio"
'Exercicio'
>>> 
>>> 
>>> 
========== RESTART: F:\CURSOS\CCPython\Week2\ContaSegundos_Dias.py ==========
Por favor, entre com o número de segundos que deseja converter: 8000000
92 dias,  14 horas,  853 minutos e 20 segundos.
>>> 
========== RESTART: F:\CURSOS\CCPython\Week2\ContaSegundos_Dias.py ==========
Por favor, entre com o número de segundos que deseja converter: 8000000
92 dias,  14 horas,  0 minutos e 20 segundos.
>>> 
========== RESTART: F:\CURSOS\CCPython\Week2\ContaSegundos_Dias.py ==========
Por favor, entre com o número de segundos que deseja converter: 8000000
92 dias,  14 horas,  13 minutos e 20 segundos.
>>> 

>>> 
>>> "TESTE"
'TESTE'
>>> 
>>> 
>>> 
========= RESTART: F:\CURSOS\CCPython\Week2\Teste_EntradadeDados.py =========
Olá

bom dia!
>>> x = input ("Qual a idade? ")
Qual a idade? 10
>>> x
'10'
>>> float(10)
10.0
>>> float(x)
10.0
>>> a = int(input("Qual o valor de a? "))
Qual o valor de a? 1
>>> b = int(input("Qual o valor de b? "))
Qual o valor de b? 2
>>> a = b
>>> b = a
>>> print(a)
2
>>> print(b)
2
>>> a = int(input("Qual o valor de a? "))
Qual o valor de a? 1
>>> b = int(input("Qual o valor de b? "))
Qual o valor de b? 2
>>> a
1
>>> b
2
>>> aux = a
>>> aux
1
>>> a = b
>>> b = aux
>>> print(a)
2
>>> print(b)
1
>>> a = 10
>>> b = 20
>>> c = a
>>> b = c
>>> a = b
>>> print(a, b, c)
10 10 10
>>> a = 10
>>> b = 5
>>> c = a + b
>>> b = 20
>>> print(a, b, c)
10 20 15
>>> A = 10
>>> a
10
>>> A
10
>>> a = 20
>>> A
10
>>> a = 2 * a
>>> A = a + A
>>> print(a)
40
>>> print ("olá" 'mundo')
olámundo
>>> 
