Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dias = total_segs // 86400
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    dias = total_segs // 86400
NameError: name 'total_segs' is not defined
>>> segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
Por favor, entre com o número de segundos que deseja converter: 85000
>>> total_segs = int(segundos_str)
>>> dias = total_segs // 86400
>>> dias
0
>>> total_segs = 8000000
>>> dias
0
>>> total_segs
8000000
>>> dias =total_segs // 86400
>>> dias
92
>>> segs_restantes = total_segs % 86400
>>> segs_restantes
51200
>>> horas = segs_restantes % 3600
>>> horas
800
>>> horas = segs_restantes // 3600
>>> horas
14
>>> segs_restantes_do_min = segs_restantes % 3600
>>> segs_restantes_do_min
800
>>> minutos = segs_restantes_do_min // 60
>>> minutos
13
>>> segs_restantes_final = segs_restantes_min % 60
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    segs_restantes_final = segs_restantes_min % 60
NameError: name 'segs_restantes_min' is not defined
>>> segs_restantes_final = segs_restantes_do_min % 60
>>> segs_restantes_final
20
>>> 
