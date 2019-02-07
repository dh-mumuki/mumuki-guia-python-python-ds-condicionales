En el ejercicio anterior analizamos este código:

```python
if dia_soleado == True:
    print('¡Qué bien, el día está soleado, salgamos a la plaza!')
```

Y comentamos que siempre y cuando el valor de **dia_soleado** sea exactamente igual a `True`, vamos a ejecutar el bloque de código que se encuentra debajo de la sentencia `if`.

Muy bien, pero... ¿qué pasa si queremos hacer algo en caso de que el día no esté soleado? Es ahí en donde entra la sentencia `else`, la contraparte del `if`. Se vería así:

```python
if dia_soleado == True:
    print('¡Qué bien, el día está soleado, salgamos a la plaza!')
else:
    print('¡Uff, qué mal, el día está feo! Mejor nos quedamos codeando ;)')

```
El condicional `else` nos permite ejecutar un bloque de código en el caso de que la condición del `if` no se cumpla, es decir, no sea verdadera. A diferencia del `if`, la estructura del `else` sólo tiene dos partes:

1. La palabra reservada `else`, seguida de dos puntos.
2. El bloque de código que se ejecuta en el caso que la condición del `if` no se cumpla, escrito en la línea siguiente y luego de una indentación (comúnmente, cuatro espacios en blanco).

Entonces, ahora que sabemos cómo funcionan el `if` y el `else`, veamos otro ejemplo: 

```python
numero = 360

if num < 180:
  print(numero, 'es menor a 180')
else:
  print(numero, 'no es menor a 180')
    
ム
> 360 no es menor a 180
```
