# Arithmetic Operations in Python
# Integers

# Ejercicio 1, Declarar tu edad como una variable entera.
edad = 19 
print("tu edad es: ", edad )
#Esta variable es de tipo entera por que no contiene decimales.

# Ejercicio 2, Declara tu estatura como una variable tipo flotante
estatura = 1.78
print("tu estatura es: ", estatura)
#Esta variable es de tipo flotante porque contiene decimales.

#Ejercicio 3, Declara una variable con un número complejo.
numero_complejo = 7j 
print("tu número complejo es: ", numero_complejo)
#Esta variable es un número complejo por la letra j.

# Ejercicio 4, Calcular el área de un triángulo.
print("Calcular el área de un triángulo")
base = int(input("Intrdocuce la base del triángulo: "))
altura = int(input("Intrdocuce la altura del triángulo: "))
área = ( 0.5 * base * altura)
print("El resultado es:", área)
#En este ejercicio uno da las medidas de la base y altura.

# Ejercicio 5, Calcular el perímetro de un triangulo.
print("Calcular el perímetro de un triangulo")
ladoA = int(input("Introduce el lado a de un triángulo: "))
ladoB = int(input("Introduce el lado b de un triángulo: "))
ladoC = int(input("Introduce el lado c de un triángulo: "))
perímetro = (ladoA + ladoB + ladoC)
print("El resultado es:", perímetro)
#En este ejercicio uno da las medidas de los lados de un triángulo.

# Ejercicio 6, Calcular la longitud y ancho de un rectángulo.
print("Calcular la longitud y ancho de un ractángulo")
longitud = int(input("Introduce la longitud del rectángulo: "))
ancho = int(input("Introduce el ancho del rectángulo: "))
área = (longitud * ancho)
perimetro = ( 2 * (longitud * ancho))
print("El resultado es:", área)
print("El resultado es:", perímetro)
#En este ejercicio uno da las medidas de la longitud y ancho.

# Ejercicio 7, Calcular el radio de un círculo.
print("Calcular el radio de un círculo")
radio = float(input("Introduce el radio de un círculo: "))
pi = (3.14)
área = (pi * radio * radio)
circunferencia = (2 * pi * radio)
print("El resultado es:", área)
print("El resultado es:", circunferencia)

# Ejercicio 8, Calcular la pendiente.
print("Cálcular la pendiente de y = 2x - 2")
##Ecuación de la línea: y = 2x - 2
m = (2) 
##Pendiente
y_intercept = -2  
##Intersección con el eje y
x_intercept = -y_intercept / m
##Intersección con el eje x
print("La pendiente (m) es:", m)
print("La intersección con el eje y es:", y_intercept)
print("La intersección con el eje x es:", x_intercept)

# Ejercicio 9, Calcular la pendiente y distancia euclidiana entre dos puntos.
print("9- Calcular la pendiente y distancia euclidiana entre (2, 2) y (6, 10)")
x1 = (2)
y1 = (2)
x2 = (6)
y2 = (10)
##Pendiente
pendiente = ((y2 - y1)/(x2 - x1))
print("La pendiente entre los puntos es:", pendiente)
##Distancia euclidiana
distancia = (((x2 - x1)**2 + (y2 - y1)**2)**0.5)
print("La distancia euclidiana entre los puntos es:", distancia)

# Ejercicio 10, Hacer una comparación de pendientes.
print("Hacer una comparación de pendientes")
comparación = m>=pendiente
print("La pendiente de la ecuación y = 2x - 2 es mayor o igual a la pendiente entre los puntos (2, 2) y (6, 10):", comparación)
comparación = m<=pendiente
print("La pendiente de la ecuación y = 2x - 2 es menor o igual a la pendiente entre los puntos (2, 2) y (6, 10):", comparación) 
comparación = m==pendiente
print("La pendiente de la ecuación y = 2x - 2 es igual a la pendiente entre los puntos (2, 2) y (6, 10):", comparación)
comparación = m!=pendiente
print("La pendiente de la ecuación y = 2x - 2 es diferente a la pendiente entre los puntos (2, 2) y (6, 10):", comparación) 
comparación = m>pendiente   
print("La pendiente de la ecuación y = 2x - 2 es mayor a la pendiente entre los puntos (2, 2) y (6, 10):", comparación)
comparación = m<pendiente
print("La pendiente de la ecuación y = 2x - 2 es menor a la pendiente entre los puntos (2, 2) y (6, 10):", comparación)

# Ejercicio 11, Calcular de y = x^2 + 6x + 9 para diferentes valores de x.
print("Calcular de y = x^2 + 6x + 9 para diferentes valores de x")
def calcular_y(x):
    return x**2 + 6*x + 9

##Probar diferentes valores de x
valores_x = [-5, -4, -3, -2, -1, 0, 1, 2, 3]
for x in valores_x:
    y = calcular_y(x)
    print(f"Para x = {x}, y = {y}")

##Solicitar un valor de x al usuario
x = float(input("Ingresa el valor de x: "))
y = calcular_y(x)
print("El valor de y es:", y)

# Ejercicio 12, Largo de "python" y "dragon" y falsa comparación.
print("Largo de 'python' y 'dragon' y falsa comparación") 
len_python = len('python')
len_dragon = len('dragon')
falsy_comparison = len_python == len_dragon
print(f"Length of 'python': {len_python}")
print(f"Length of 'dragon': {len_dragon}")
print(f"Falsy comparison (length of 'python' == length of 'dragon'): {falsy_comparison}")

# Ejercicio 13, Checar si "on" está en "python" y "dragon".
print("Checar si 'on' está en 'python' y 'dragon'")
on_in_both = 'on' in 'python' and 'on' in 'dragon'
print(f"'on' in both 'python' and 'dragon': {on_in_both}")

# Ejercicio 14, Checar si "jargon" está en la frase.
print("Checar si 'jargon' está en la frase")
frase = "I hope this course is not full of jargon"
jargon_in_frase = 'jargon' in frase
print(f"'jargon' in the frase: {jargon_in_frase}")

# Ejercicio 15, No hay "on" en "python" y "dragon".
print("No hay 'on' en 'python' y 'dragon'")
no_on_in_both = 'on' not in 'python' and 'on' not in 'dragon'
print(f"'on' not in both 'python' and 'dragon': {no_on_in_both}")

# Ejercicio 16, Convertir la longitud de "python" a float y luego a string.
print("Convertir la longitud de 'python' a float y luego a string")
len_python = len('python')
len_python = float(len_python)
print(type(len_python))
len_python = str(len_python)
print(type(len_python))
print(f"Length of 'python' as string: {len_python}")
print(type(len_python))

# Ejericio 17, Checar si un número es par.
print("Checar si un número es par")
numero = int(input("Ingresa un número: "))
es_par = (numero % 2 == 0)
print(f"El número {numero} es par: {es_par}")

# Ejercicio 18, Check if floor division of 7 by 3 is equal to int converted value of 2.7.
print("Check if floor division of 7 by 3 is equal to int converted value of 2.7")
floor_division = 7 // 3
int_conversion = int(2.7)
equal = floor_division == int_conversion
print(f"Floor division of 7 by 3: {floor_division}")
print(f"Int converted value of 2.7: {int_conversion}")
print(f"Equal: ", equal)

# Ejercicio 19, Checar si el tipi de "10" es igual al tipo de 10.
print("Checar si el tipo de '10' es igual al tipo de 10")
type_comparison = type('10') == type(10)
print(f"Type of '10' is equal to type of 10: {type_comparison}")

# Ejercicio 20, Checar si int("9.8") es igual a 10
print("Checar si int('9.8') es igual a 10")
try:
    int_value = int('9.8')
except ValueError:
    int_value = None
comparison = int_value == 10
print(f"int('9.8') is equal to 10: {comparison}")

# Ejercicio 21, Calcular el pago basado en horas y tarifa por hora.
print("Calcular pago basado en horas y tarifa por hora")
horas = float(input("Introduce el número de horas trabajadas: "))
tarifa = float(input("Introduce la tarifa por hora: "))
pago = ( horas * tarifa)
print(f"El pago es: ", pago)

# Ejercio 22, Escribe un script que le pida al usuario que ingrese el número de años.
# Calcular el número de segundos que una persona puede vivir. 
print("Calcular el número de segundos que una persona puede vivir")
años = int(input("Ingresa el número de años: "))
segundos_por_año = (365 * 24 * 60 * 60)
segundos_vividos = (años * segundos_por_año)
print(f"Una persona puede vivir {segundos_vividos} segundos")

# Ejercicio 23, Escribir un Script para mostrar la siguiente tabla.
print("Escribir un Script para mostrar la siguiente tabla")
print("a  a^0  a^1  a^2  a^3")
for a in range(1, 6):
    print(f"{a}  {a**0}  {a**1}  {a**2}  {a**3}")