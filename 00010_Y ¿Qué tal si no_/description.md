En el ejercicio anterior analizamos el siguiente código:

```python
if diaSoleado == true :
   print ('¡Qué bien¡ Salgamos a la plaza')

```

Y comentamos que siempre y cuando el valor de **diaSoleado** sea exactamente igual a `true`, vamos a ejecutar el bloque de código que se encuentra debajo.

Muy bien, pero ¿Qué pasa si queremos hacer algo en caso de que el día no esté soleado?. Es ahí en donde entra el `else`, la contraparte del `if`. Se vería así:

```python
if diaSoleado == true :
    print ('¡Qué bien¡ Salgamos a la plaza') 
else :
    print ('¡Uff que mal! mejor nos quedamos codeando')

```
El condicional `else` nos permite ejecutar un bloque de código, en el caso que la condición del `if` no se cumpla, es decir, no sea verdadera. A diferencia del `if`, la estructura del `else` solo tiene 2 partes:

1. La palabra reservada `else`.
2. El bloque de código que se ejecuta en el caso que la condición del `if` no se cumpla.

Entonces, ahora que sabemos cómo funcionan el `if` y `else`, veamos otro ejemplo: 

```python
 num_3 = 360

    if num_3 < 180:
        print(num_3, 'es menor a 180')
    else:
        print(num_3, 'no es menor a 180')
    
ム
> 360 no es menor a 180
```


