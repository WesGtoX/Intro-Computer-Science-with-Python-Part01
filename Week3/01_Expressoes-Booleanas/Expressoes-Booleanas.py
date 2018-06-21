Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 5 > 3
True
>>> 18 == 9 * 2
True
>>> x = 12312
>>> x < 0
False
>>> type(False)
<class 'bool'>
>>> type(x > 0)
<class 'bool'>
>>> x > 0 and x 8 **2 > 100
SyntaxError: invalid syntax
>>> x > 0 and x = **2 > 100
SyntaxError: invalid syntax
>>> x > 0 and x = ** 2 > 100
SyntaxError: invalid syntax
>>> x> 0 and x **2 > 100
True
>>> x < 0 and x == 12312
False
>>> x < 0 or x == 12312
True
>>> x > 0
True
>>> not x > 0
False
>>> not False
True
>>> not True
False
>>> not not True
True
>>> 
>>> 
>>> 
>>> fizerSol = True
>>> forFeriado = False
>>> vouParaPraia = fizerSol and forFeriado
>>> vouParaPraia
False
>>> forFeriado = True
>>> vouParaPraia = fizerSol and forFeriado
>>> vouParaPraia
True
>>> 
>>> 
>>> paitrocinio = False
>>> rolarPromoção = True
>>> vouAoShow = paitrocinio or rolarPromoção
>>> vouAoShow
True
>>> 
>>> y = 50
>>> 
>>> 
>>> 
>>> 
>>> (x > 0) and not (y == 50) or (x + y == 150)
False
>>> 
>>> 
>>> 
>>> 'TESTE'
'TESTE'
>>> x = 5
>>> 
>>> (x!=0) and (x==0)
False
>>> True and (4=>3)
SyntaxError: invalid syntax
>>> True and (4 => 3)
SyntaxError: invalid syntax
>>> (x > 0) or x <= 0)
SyntaxError: invalid syntax
>>> (x > 0) or (x <= 0)
True
>>> (-10 < x < 0)
False
>>> not (x > 0) and (x > 0)
False
>>> 
>>> 
>>> x = 5
>>> y = 3
>>> x > y
True
>>> z = 7
>>> x > y and x < z
True
>>> 
>>> 
>>> idade = 15
>>> maioridade = 18
>>> pode_dirigir = idade >= maioridade
>>> print (pode_dirigir)
False
>>> fruta = laranja
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    fruta = laranja
NameError: name 'laranja' is not defined
>>> 
>>> x = 10
>>> y = 15
>>> z = 25
>>> print((x == z - y) and (z != y - x) or not (y != z - x))
True
>>> 
>>> x = 10
>>> y = 20
>>> z = 30
>>> print( <= 30) and y >= 5
SyntaxError: invalid syntax
>>> print(x <= 30 andy >= 5
      
SyntaxError: invalid syntax
>>> print(x <= 30 and y >= 5)
True
>>> print(not y < 10 or not z == 10)
True
>>> print(x >= 10 or y != z - x)
True
>>> print(not y > 10 or not z > 10)
False
>>> type(dados)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    type(dados)
NameError: name 'dados' is not defined
>>> type(or)
SyntaxError: invalid syntax
>>> type(and)
SyntaxError: invalid syntax
>>> type(False)
<class 'bool'>
>>> 
>>> 
>>> a = 1
>>> b = 2
>>> a != 1 or b == 1
False
>>> a != 1
False
>>> a == 2 and b != 1
False
>>> not (a == 1)
False
>>> a != 2 or b == 1
True
>>> 
