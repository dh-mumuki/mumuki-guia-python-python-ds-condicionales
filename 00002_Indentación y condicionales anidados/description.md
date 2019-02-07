#### Indentación

En Python, lo que determina la forma en la que se encuentra estructurado el código es la **indentación**. Podemos pensar en la indentación como la sangría que dejamos al inicio de cada línea de código.

Por lo tanto, los bloques de código vienen definidos por la cantidad de espacios en blanco que hay al comienzo de cada línea.

Veamos estos ejemplos con expresiones condicionales: 

  ``` python
if True:
    #en este nivel va el código que pertenece al bloque del if
    print(1)
    print(2)
    print('Etc.')
#en este nivel estamos fuera del primer if
print('Terminó')

ム
> 1
> 2
> Etc.
> Terminó
  ```

En este primer ejemplo podemos observar que el efecto del `if` va desde el `print(1)`, hasta el `print('etc').

Lo que determina el final del alcance del bloque de código que pertenece al `if` es la vuelta al nivel de indentación previo (sin ningún espacio en blanco al inicio de la línea).

  ``` python
if False:
    #en este nivel va el código que pertenece al bloque del if
    print(1)
    print(2)
    print('Etc.')
#en este nivel estamos fuera del primer if
print('Terminó')

ム
> Terminó
  ```
Como se puede observar en ambos ejemplos, siempre se ejecuta el `print('Terminó'), sin embargo, el bloque que pertenece al `if` sólo se ejecuta en el primer ejemplo, en donde la condición se evalúa a `True`.

Entonces, el indicador de que una sentencia pertenece o no a un bloque depende de la indentación.

#### Condicionales anidados

Es posible realizar una evaluación sobre expresiones condicionales dentro del bloque de código que corresponde al resultado de una evaluación de otra expresión. Por ejemplo:


``` python
if 3 > 1:
    # Código correspondiente al primer if
    if 2 < 3:
        # Código correspondiente al segundo if
        print('Las dos condiciones son correctas')
    # Vuelta del código correspondiente al primer if
    print('3 es mayor que 1')

ム
> Las dos condiciones son correctas
> 3 es mayor que 1
```

En esta demostración podemos observar la importancia de los espacios al momento de definir el alcance de cada bloque de código. Este alcance toma importancia cuando utilizamos el código alternativo mediante el uso del `if`... `elif`... `else`.  

``` python
num = 4
if num % 2 == 0:
    # dentro de este nivel se cumple que num dividido 2 no tiene resto
    if num > 0:
        # dentro de este nivel se sigue cumpliendo que num dividido 2 no tiene resto
        # pero, además, num es positivo
        print('Las dos condiciones son correctas')
    else:
        # este else corresponde al segundo if
        # dentro de este else, num no es mayor que cero.
        print(num, 'no es mayor que cero')
else:
    # este else corresponde al primer if
    # dentro de este else, num dividido 2 tiene decimales
    print(num, 'dividido 2 tiene resto')
```
<br>

***
**Dado el siguiente código:**

``` python
if num > 5:
    print('a')
    if num % 2 == 0:
        print('b')
    else:
        print('c')
else:
    print('d')
```
> :memo: **¿Cuál de las siguientes afirmaciones es verdaderas?**