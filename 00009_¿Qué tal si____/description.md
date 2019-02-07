Ninguna introducción a Python estaría completa sin mostrar la estructura de control condicional conocida como `if`.<br>
El `if` nos permite ejecutar un código sujeto a una condición.

Un ejemplo de la vida real podría ser:
**¡Si el día está soleado, vamos a la plaza!**. Aquí estamos **condicionando** nuestra salida a la plaza si y sólo si el día está soleado.

Ahora bien, ¿cómo podemos llevar esto a código? Primero, deberemos entender que la estructura del `if` se divide en tres partes:

1. La palabra reservada `if`.
2. La condición que queremos evaluar, seguida de dos puntos.
3. El bloque de código que se ejecuta en el caso que la condición evaluada se cumpla (es decir, sea `True` -verdadera-), en la siguiente línea y luego de una indentación (comúnmente, cuatro espacios en blanco).

Veamos un ejemplo:

```python
numero = 43

if numero > 0:
    print('El número es positivo')

ム
> 'El número es positivo'
```

Ahora, ¿qué podríamos hacer para codificar nuestra salida a la plaza?

Veámoslo:

```python
if dia_soleado == True:
    print('¡Qué bien, el día está soleado, salgamos a la plaza!')

ム
> ¡Qué bien, el día está soleado, salgamos a la plaza!'
```

Si prestaste atención, te habrás dado cuenta de que para comparar `dia_soleado` con `True` utilizamos `==`. Se hace de esta manera porque si usáramos un solo `=`, sería como si estuviéramos definiendo una variable, que no es lo que queremos hacer en este caso.

En el ejemplo anterior, `dia_soleado` es una variable que almacena un valor booleano, y siempre y cuando ese valor sea exactamente igual a `True`, vamos a ejecutar el bloque de código que se encuentra debajo, en este caso, el `print()`. Va tomando más sentido, ¿no?

Hagamos una pequeña práctica para ir asentando estos conceptos:

> :memo: **Declará la variable `dia_de_semana` y asignale el valor `'domingo'`. Luego, implementá un condicional usando el `if` que evalúe si el `dia_de_semana` es `'domingo'` y, si esto es verdadero, que imprima por pantalla `'Hoy se juega al futbol!!!'`.**