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

Retomemos los ejemplos del <a href=#/guides/dh-mumuki/mumuki-guia-python-python-ds-condicionales/exercises/4 >enunciado anterior </a>, pero ahora vamos a utilizar los condicionales para darle un sentido a las evaluaciones:

  * Si un número es mayor a otro número, entonces...
      
      ``` python
    if 3 > 2:
      print('Es mayor')
    ```
    _Salida:_
**> Es mayor**

En este último caso podemos observar la utilidad del `if`, ya que, en función al resultado de una expresión, podemos tomar determinadas decisiones.

  * Si la cantidad de elementos (caractéres) en una palabra es igual a una magnitud dada, imprime 'tiene pocos elementos'
      
      ``` python
    if len('Python') == 3:
      print('tiene pocos elementos')
    ```
    _Salida:_ 
**>**

En este caso, la cantidad de caracteres en 'Python' no es igual a 3, por lo tanto el codigo dentro del condicional `if` no se ejecutará.

  * Si el resultado de una operación numérica es igual al resultado de otra, entonces multiplica 3x8 e imprime el resultado.
      
      ``` python
    if 2*2 == 2**2:
      print(3*8)
    ```
    _Salida:_
**> 24**

  * si existe un elemento dado en una lista, entonces imprime 'lo encontre'.
      
      ``` python
    if 'pingüino' in ['ballena', 'pingüino', 'pulpo']:
      print('lo encontre')
    ```
    _Salida:_
  **> 'lo encontre'**



  * Supongamos que debemos evaluar dos variables, ambas son enteros, y queremos declarar algunos predicados condicionales relacionados con la magnitud de estas variables.

  ``` python
  num_1 = 90
  num_2 = 180
  num_3 = 360
  
  if num_1 < 180:
      print(num_1, 'es menor a 100')
  
  if num_2 < 180:
      print(num_2, 'es menor a 100')
      
  if num_3 < 180:
      print(num_3, 'es menor a 100')
  ```
  _Salida:_
  **> 360 es menor a 100**

Como podemos observar en esta demostración, solo los `if` en donde el resultado es `True`, ejecutan el código correspondiente a las 