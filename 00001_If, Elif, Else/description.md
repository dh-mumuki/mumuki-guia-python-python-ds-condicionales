Ahora vamos a utilizar las expresiones condicionales como una herramienta de decisión. Para eso, veamos cómo se comporta el llamado `if`.  Recordemos: en Python el valor `True` es un un tipo de datos booleano que quiere decir verdadero.<br>

Como el valor `True` siempre es verdadero. Entonces el código dentro del `if`, que se encuentra a un nivel más de [indentación](https://es.wikipedia.org/wiki/Indentaci%C3%B3n), se ejecuta. 

``` python
if True:
    print('entré en el primer if')
    
ム
> entré en el primer if 
```

``` python
if False:
    print('entré en el segundo if')
    
ム
> 
```

El resultado de la evaluación del `False` es siempre falso. Por esa razón, el código dentro de este segundo condicional nunca va a ser ejecutado.

Retomemos los ejemplos del [enunciado anterior](href=#/guides/dh-mumuki/mumuki-guia-python-python-ds-condicionales/exercises/4) pero ahora vamos a utilizar los condicionales para darle un sentido a las evaluaciones:

  * Si un número es mayor a otro número, entonces...
      
``` python
if 3 > 2:
    print('Es mayor')
        
ム
> Es mayor
```

En este último caso podemos observar la utilidad del `if`, ya que, en función al resultado de una expresión podemos tomar determinadas decisiones. En este caso imprimir: 'Es mayor'

  * Si la cantidad de elementos (caracteres) en una palabra es igual a una magnitud dada, imprime: 'tiene pocos elementos'
      
``` python
if len('Python') == 3:
    print('tiene pocos elementos')
        
ム
>
```

En este caso la cantidad de caracteres en `Python` no es igual a 3, por lo tanto, el código dentro del condicional if no se ejecutará.

  * Si el resultado de una operación numérica es igual al resultado de otra, entonces multiplica 3x8 e imprime el resultado.
      
``` python
if 2*2 == 2**2:
    print(3*8)
        
ム
>24 
```

  * Si existe un elemento dado en una lista, entonces imprime 'lo encontre'.
      
``` python
if 'pingüino' in ['ballena', 'pingüino', 'pulpo']:
    print('lo encontre')
        
ム
> lo encontré
    ```

  * Supongamos que debemos evaluar dos variables, ambas son enteros, y queremos declarar algunos predicados condicionales relacionados con la magnitud de estas variables.

``` python
num_1 = 90
num_2 = 180
num_3 = 360
    
if num_1 < 180:
    print(num_1, 'es menor a 180')

if num_2 < 180:
    print(num_2, 'es menor a 180')
        
if num_3 < 180:
    print(num_3, 'es menor a 180')
        
ム
> 360 es menor a 100
```

Como podemos observar en esta demostración, solo los if en donde el resultado es True ejecutan el código correspondiente.  

Ahora bien, es posible ejecutar código alternativo cuando no se cumple la condición declarada en el if una de las formas es hacer un llamado al else.<br>

### Ejecutando código alternativo... (`if`/`else`)

Cuando no se cumple una condición dada en `if`, es posible ejecutar un bloque de código alternativo, una forma es utilizar una llamada al `else`.

El código dado en `elif` o `else` se ejecuta **siempre** que no se cumpla la condición `if` (en un esquema `if`/`else`).

Para utilizar un esquema `if`/`else`, ambos tienen que estar al mismo nivel de <a href=https://es.wikipedia.org/wiki/Indentaci%C3%B3n> indentación </a>. 

  ``` python
    num_3 = 360

    if num_3 < 180:
        print(num_3, 'es menor a 180')
    else:
        print(num_3, 'no es menor a 180')
    ム
    > 360 no es menor a 180
  ```

Como se puede observar en este último ejemplo, no existe precedencia de una expresión lógica despúes del `else`, ya que la ejecución del código del `else`, en este esquema, depende de la evaluación realizada en el `if`: 
  
  * si el `if` es verdadero, entonces no se ejecuta el código en el `elif` o `else`
  * si la expresión en `if` es falsa, entonces se ejecuta el código en `elif` o `else`.


### Ejecutando código alternativo... (`if`/`elif`/`else`).

Además es posible tomar decisiones utilizando un conjunto de expresiones condicionales alternativas, esto podría ser útil cuando se desean tomar mas de dos decisiones sobre estos conjuntos de expresiones.


``` python
num = 10

if num < 10:
    print('es menor que 10')

elif num == 10:
    print('es igual a 10')
    
else:
    print('no es ni igual ni menor a 10')

ム
> 24

```

<br>
****
**Veamos el siguiente código**

``` python
if num > 1 or num < 1:
    print("primer if")
else:
    print("primer else")
```

> :memo:**¿Cúal de los enunciados es el verdadero?**