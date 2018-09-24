Para poder construir un programa, se deben utilizar expresiones en donde se tengan que llevar a cabo evaluaciones basadas en las propiedades de algún dato.

Estas evaluaciones pueden dar como resultado 2 tipos de valores en python: True o False. El comportamiento de un programa puede encontrarse determinado por la forma en los que estos predicados son evaluados.

**Introducción al uso de condicionales.**

Los condicionales son estructuras de control en python y sirven para evaluar un predicado en terminos booleanos (que la sentencia se cumpla o no), entre los condicionales principales encontramos las estructuras de control **if**, **if-else**, **if-elif-else**:
          
  * `if`: Evalúa una expresion y si el resultado de la evaluación es verdadera, se ejecuta el código indentado en el proximo nivel. Cuando la evaluación da un resultado falso, no se ejecuta el código contenido dentro del if y se busca un else o un elif en el mismo nivel de indentación, si no existe se continúa con la ejecución, saltando el código contenido dentro del if
  * `elif`: Evalúa una expresión, pero a diferencia del `if` el `elif` viene de un nivel de indentación en donde una evaluación previa resulto falsa (o sea viene despues de un if u otro elif).
  * `else`: Cuando todas las expresiones al mismo nivel resultan negativas, se ejecuta el código contenido 

