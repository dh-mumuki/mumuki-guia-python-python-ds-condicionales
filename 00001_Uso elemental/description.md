En este Ejercicio vamos a mostrar como se comporta el `if`, en python el valor `True` es un <a href=https://es.wikipedia.org/wiki/Tipo_de_dato_l%C3%B3gico > un tipo de datos booleano </a>que quiere decir verdadero.

Como el valor `True` siempre da como resultado verdadero, entonces el código dentro del `if` (que se encuentra a un nivel más de <a href=https://es.wikipedia.org/wiki/Indentaci%C3%B3n> indentación </a>) se ejecuta.

``` python
if True:
  print('entré en el primer if')
```
_Salida:_
**> entre en el primer if**

``` python
if False:
  print('entré en el segundo if')
```
_Salida:_
**>**


El resultado de la evaluación del `False` es siempre falso, por esa razón el código dentro de este segundo condicional, nunca va a ser ejecutado.
