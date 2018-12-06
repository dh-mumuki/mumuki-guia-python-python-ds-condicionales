Ninguna introducción a Python estaría completa sin mostrar la estructura de control condicional conocida como `if`. <br>
El `if` nos permite ejecutar un código según una condición.

Un ejemplo de la vida real podría ser:
**¡Si el día está soleado, vamos a la plaza!**. Como podés ver en el ejemplo anterior estamos **condicionando** nuestra salida a la plaza si y solo si está soleado.

Ahora bien ¿Cómo podemos llevar esto a código? Primero deberemos entender que la estructura del `if` se divide en 3 partes:

1. La palabra reservada `if`.
2. La condición que queremos evaluar, seguida de `:`
3. El bloque de código que se ejecuta en el caso que la condición evaluada se cumpla (es decir, sea `true` -verdadera-), en la siguiente línea.

Veamos un ejemplo:

```python
numero = 43;

if numero > 0:
    print('El número es positivo')
    
ム
> 'El número es positivo'
```

Ahora ¿Qué podríamos hacer para codificar nuestra salida a la plaza?

Veámoslo:

```python
if dia_soleado == True:
    print('¡Qué bien¡ Salgamos a la plaza')

ム
> ¡Qué bien¡ Salgamos a la plaza'
```

En el ejemplo anterior, `dia_soleado` sería una variable que almacena un valor booleano, y siempre y cuando ese valor sea exactamente igual a `True`, vamos a ejecutar el bloque de código que se encuentra debajo, en ese caso, el `print()`. Va tomando más sentido ¿No?

Hagamos una pequeña práctica para ir asentando el concepto. 

> :memo:**Declará la variable `dia_de_semana` y asignale el valor `"domingo"`. Luego implementa un condicional usando el `if` que compare la igualdad de `dia_de_semana` con el día `"domingo"`, y si es verdadero que imprima por pantalla `"Hoy se juega al futbol!!!"`.**