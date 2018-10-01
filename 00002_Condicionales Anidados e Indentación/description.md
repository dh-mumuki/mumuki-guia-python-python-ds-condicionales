### Condicionales Anidados e Indentación.

#### Indentación.

En Python, lo que determina la forma en la que se encuentra agrupado el código, es la indentación.

Por lo tanto, los bloques de código vienen dados por la cantidad de espacios desde el comienzo de linea.

Veamos estos ejemplos con expresiones condicionales, 

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

En este primer ejemplo, podemos observar que el efecto del `if` va desde el `print` de '1', hasta el `print` de 'etc'.

Lo que determina el final del alcance del bloque de código que pertenece al `if`, es la vuelta al nivel de indentación previo.

  ``` python
if False:
  #en este nivel va el código que pertenece al bloque del if
  print(1)
  print(2)
  print('etc')
#en este nivel estamos fuera del primer if
print('termino')
  ```
  _Salida:_
  
**> termino**  

Como se puede observar, en ambos ejemplos siempre se ejecuta el `print` que imprime "termino", sin embargo, el bloque que pertenece al `if`, se ejecuta en función al resultado de la evaluacion de la expresion dada.

Entonces el indicador de que una sentencia pertenece o no al bloque, depende de la indentación.

#### Condicionales anidados.

Es posible realizar una evaluación sobre expresiones condicionales dentro del bloque de código que corresponde al resultado de una evaluación de otra expresión.


``` python
if 3 > 1:
    # Código correspondiente al primer if
    if 2 < 3:
        # Código correspondiente al segundo if
        print('las dos condiciones son correctas')
    # Vuelta del código correspondiente al primer if
```

En esta demostración podemos observar la importancia de los espacios, al momento de definir el alcance de cada bloque de código. Este alcance toma importancia cuando utilizamos el código alternativo mediante el uso del `if`/`elif`/`else`


