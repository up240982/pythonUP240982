# Arithmetic Operations in Python
# Integers

# Ejercicio 1, Declarar tu edad como una variable entera .
edad = 20 
print("tu edad es: ", edad )
#esta variable es de tipo entera por que no contiene decimales.

# Ejercicio 2, Declara tu estatura como una variable tipo flotante
estatura = 1.78
print("tu estatura es: ", estatura)
#esta variable es de tipo flotante porque contiene decimales.

#Ejercicio 3, Declara una variable con un numero complejo.
numerocomplejo = 7j 
print("tu numero complejo es: ", numerocomplejo)
#esta variable es un numero complejo por la letra j.

#Ejercicio 4, Calcular el area de un traingulo.
print("Calcular el area de un traingulo")
base = int(input("Intrdocuce la base del triangulo: "))
altura = int(input("Intrdocuce la altura del triangulo: "))
area = ( 0.5 * base * altura )
print("El resultado es:", area )

#Ejercicio 5, Calcular el perimetro de un triangulo.
print("Calcular el perimetro de un triangulo")
ladoA = int(input("Introduce el lado a de un triangulo: "))
ladoB = int(input("Introduce el lado b de un triangulo: "))
ladoC = int(input("Introduce el lado c de un triangulo: "))
perimetro = (ladoA + ladoB + ladoC)
print("El resultado es:", perimetro)

#Ejercicio 6, Calcular la longitud y ancho de un rectangulo.
print("Calcular la longitud y ancho de un ractangulo")
longitud = int(input("Introduce la longitud del rectangulo: "))
ancho = int(input("Introduce el ancho del rectangulo: "))
area = (longitud*ancho)
perimetro = (2*(longitud*ancho))
print("El resultado es:", area)
print("El resultado es:", perimetro)

#Ejercicio 7, Calcular el radio de un circulo.
print("Calcular el radio de un circulo")
radio = float(input("Introduce el radio de un circulo: "))
pi = 3.14
area = (pi*radio*radio)
circunferencia = (2*pi*radio)
print("El resultado es:", area)
print("El resultado es:", circunferencia)

#Ejercicio 8, 