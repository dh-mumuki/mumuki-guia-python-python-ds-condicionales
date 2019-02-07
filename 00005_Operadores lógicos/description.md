Los operadores lógicos permiten unir un conjunto de evaluaciones distintas en una sola expresión más compleja.

En Python, estos operadores son:
  
* `not`: Niega una expresión.
* `and`: Evalúa potencialmente dos expresiones; si ambas son verdaderas, devuelve `True`, pero si alguna o ambas son falsas, devuelve `False`.
* `or`: Evalúa potencialmente dos expresiones; si alguna es verdadera, devuelve `True`, pero si ambas son falsas, devuelve `False`.

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
# len(lista) devuelve la cantidad de elementos contenidos en la lista
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

> :memo: **¿Cuáles de estas expresiones se evalúan como `True`? Considerar las siguientes variables:** <br> 
**A = True <br>
B = True <br>
C = False <br>**
