Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 10
10
>>> 
>>> 
>>> type(10)
<class 'int'>
>>> type("tudo bem?")
<class 'str'>
>>> 
>>> 
>>> 5 / 2
2.5
>>> type(5 / 2)
<class 'float'>
>>> 10 /3
3.3333333333333335
>>> 10 // 3
3
>>> 10 % 3
1
>>> 1540 % 5658
1540
>>> peso = 78
>>> altura = 1.83
>>> 
>>> 
>>> peso
78
>>> type(altura)
<class 'float'>
>>> 
>>> altura
1.83
>>> 
>>> IMC
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    IMC
NameError: name 'IMC' is not defined
>>> IMC = peso / (altura **2)
>>> IMC
23.291229956104985
>>> 
>>> 
>>> 
>>> 
>>> 
>>> IMCInteiro = int(IMC)
>>> 
>>> 
>>> 
>>> IMCInteiro
23
>>> 
>>> 
>>> 
>>> texto = "Bom dia, tudo bem?"
>>> texto
'Bom dia, tudo bem?'
>>> 
>>> 
>>> len(texto)
18
>>> 
>>> 
>>> len(IMC)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    len(IMC)
TypeError: object of type 'float' has no len()
>>> 
>>> 
>>> 
>>> 
>>> 
>>> temp = str(texto)
>>> temp
'Bom dia, tudo bem?'
>>> 
>>> 
>>> temp = str(IMC)
>>> 
>>> temp
'23.291229956104985'
>>> len(IMC)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    len(IMC)
TypeError: object of type 'float' has no len()
>>> len(temp)
18
>>> len(str(IMC))
18
>>> temp
'23.291229956104985'
>>> IMC = str(temp)
>>> IMC
'23.291229956104985'
>>> len(IMC)
18
>>> IMC = float
>>> imc
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    imc
NameError: name 'imc' is not defined
>>> IMC
<class 'float'>
>>> IMC = str
>>> IMC
<class 'str'>
>>> IMC = peso / (altura **2)
>>> IMC
23.291229956104985
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 10 // 3
3
>>> c=ola
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    c=ola
NameError: name 'ola' is not defined
>>> c = "ola"
>>> n = "ana"
>>> t = "bom dia"
>>> len(c + n + t)
13
>>> len(c) + len(n) + len(t)
13
>>> 22 % 3
1
>>> 22 / 3
7.333333333333333
>>> 2*1**2
2
>>> 
>>> 
>>> 
>>> int(x)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    int(x)
NameError: name 'x' is not defined
>>> str
<class 'str'>
>>> int(2.333)
2
>>> IMC
23.291229956104985
>>> IMC = str
>>> IMC
<class 'str'>
>>> IMC = str
>>> _a=1
>>> 
>>> _a
1
>>> __a=1
>>> __a
1
>>> __st__=
SyntaxError: invalid syntax
>>> __st__=1
>>> __st__
1
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> c
'ola'
>>> n
'ana'
>>> t
'bom dia'
>>> print (len(cumprimento + nome + turno))
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    print (len(cumprimento + nome + turno))
NameError: name 'cumprimento' is not defined
>>> print (len(c + n + t))
13
>>> tamanho = len(c) + len(n) + len(t)
>>> tamanho
13
>>> len(c) + len(n) + len(t)
13
>>> 10/3
3.3333333333333335
>>> 10//3
3
>>> 22 % 3
1
>>> 2*1**2
2
>>> 
