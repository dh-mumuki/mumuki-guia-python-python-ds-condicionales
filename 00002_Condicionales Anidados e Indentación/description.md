### Condicionales Anidados e Indentación.

En Python, lo que determina la forma en la que se encuentra agrupado el código, es la indentación.

Por lo tanto, los bloques de código vienen dados por la cantidad de espacios desde el comienzo de linea.

Veamos estos ejemplos con expresiones condicionales:

  ``` python
if True:
  #en este nivel va el código que pertenece al bloque del if
  print(1)
  print(2)
  print('etc')
#en este nivel estamos fuera del primer if
print('termino')
  ```
  _Salida:_
  
**> 1**  
**> 2**  
**> etc**  
**> termino**  


