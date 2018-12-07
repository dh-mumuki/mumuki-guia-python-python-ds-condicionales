Los operadores lógicos o booleanos permiten unir un conjunto de evaluaciones separadas en una sola expresión más compleja.

En python3 estos operadores son 3 `not`, `and` y `or`.
  
* `not` : Niega una expresión.
* `and` : Evalúa potencialmente dos expresiones, si ambas son verdaderas devuelve verdadero, si alguna o ambas son falsas devuelve falso.
* `or`  : Evalúa potencialmente dos expresiones, si alguna es verdadera, devuelve verdadero, si ambas son falsas, devuelve falso.


### Ejemplos

Observemos con cuidado las siguientes expresiones para ver cómo se comportan los operadores:

  ``` python
not False

ム
> True
  ```

  ``` python
not 3 > 2

ム
> False
  ```

  ``` python
True and True

ム
> True
  ```

  ``` python
True and False

ム
> False
  ```
  
  ``` python
# len(lista) devuelve la cantidad de elementos
3 < 5 and len([1,2,3]) == 3

ム
> True
  ```

  ``` python
True or False

ム
> True
  ```

  ``` python
2 < 1 or -1 < 3

ム
> True
  ```

<br>

> :memo: **¿Cuáles de estas expresiones evalúan `TRUE`? Considerar las siguientes variables:** <br> 
**A = True <br>
B = True <br>
C = False <br>**
