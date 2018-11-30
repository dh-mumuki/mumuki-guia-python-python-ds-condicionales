### Operadores lógicos.

Los operadores lógicos o booleanos permiten unir un conjunto de evaluaciones separadas, en una sola expresión mas compleja.

En python3 estos operadores son 3 `not`, `and` y `or`.
  
* `not` : Niega una expresión.
* `and` : Evalúa potencialmente dos expresiones, si ambas son verdaderas devuelve verdadero, si alguna o ambas son falsas devuelve falso.
* `or`  : Evalúa potencialmente dos expresiones, si alguna es verdadera, devuelve verdadero, si ambas son falsas, devuelve falso.


### Ejemplos

Observemos con cuidado las siguientes expresiones para ver cómo se comportan los operadores:

  ``` python
not False
  ```
  _Salida:_
**> True**

  ``` python
not 3 > 2
  ```
  _Salida:_
**> False**


  ``` python
True and True
  ```
  _Salida:_
**> True**

  ``` python
True and False
  ```
  _Salida:_
**> False**

  ``` python
# len(lista) devuelve la cantidad de elementos
3 < 5 and len([1,2,3]) == 3
  ```
  _Salida:_
**> True**

  ``` python
True or False
  ```
  _Salida:_
**> True**

  ``` python
2 < 1 or -1 < 3
  ```
  _Salida:_
**> True**
<br>

**¿Cuáles de estas expresiones evalúan `TRUE`? Considerar las siguientes variables:** 
* A = True
* B = True
* C = False
