### Operadores lógicos.

Los operadores lógicos o booleanos permiten unir un conjunto de evaluaciones separadas, en una sola expresión mas compleja.

En python3 estos operadores son 3 `not`, `and` y `or`.
  
* `not` : Niega una expresión.
* `and` : Evalúa potencialmente dos expresiones, si ambas son verdaderas devuelve verdadero, si alguna o ambas son falsas devuelve falso.
* `or`  : Evalúa potencialmente dos expresiones, si alguna es verdadera, devuelve verdadero, si ambas son falsas, devuelve falso.


### Ejemplos

      
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
