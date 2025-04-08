##Ejercicios de Nivel 1
print("Ejercicios de Nivel 1:")

# Ejercicio 1, Explain the difference between map, filter, and reduce.
print("Ejercicio 1:")
print("La diferencia entre map, filter y reduce es que:")
#map: aplica una funcion a cada elemento de una lista y devuelve una nueva lista con los valores transformados. 
#se usa para modificar elementos.
#ejemplo:
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print("Lista original:", numeros)
print("Lista de cuadrados:", cuadrados)
#filter: filtra los elementos de una lista segun una condicion, devolviendo solo aquellos que cumplen con el criterio.
#se usa para seleccionar elementos especificos.
#ejemplo:
numeros = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Lista original:", numeros)
print("Lista de pares:", pares)
#reduce: aplioca una operacion acumulativa sobre los elementos de una lista, reduciendolo a un solo valor.
#se usa para calcular resultados agregados.
#ejemplo:
from functools import reduce
numeros = [1, 2, 3, 4, 5]
producto = reduce(lambda x, y: x * y, numeros)
print("Lista original:", numeros)
print("Producto de la lista:", producto)

# Ejercicio 2, Explain the difference between higher order function, closure and decorator.
print("Ejercicio 2:")
print("La diferencia entre higher order function, closure y decorator es que:")
#higuer order function: funciones que reciben otras funciones como argumentos o que te devuelven una funcion como resultado.
#se usan para escribir codigo mas flexible y reutilizable.
#ejemplo:
def aplicar_funcion(funcion, valor):    
    return funcion(valor)
doble = lambda x: x * 2
resultado = aplicar_funcion(doble, 5)
print("Resultado de aplicar la funcion doble:", resultado)
#closure: funcion que recuerda el entorno en el que se creo, incluso cuando se ejecuta fuera de ese entorno.
# se usa para permitir mantener estados sin necesidad de usar variables globales. 
#ejemplo:
def crear_multiplicador(factor):
    def multiplicador(numero):
        return numero  * factor
    return multiplicador
multiplica_por_3 = crear_multiplicador(3)
print("Resultado de la closure:", multiplica_por_3(5))
#decorator: funcion que modifica el comportamiento de otra funcion sin cambiar su codigo.
#se usa mucho para extender funcionalidades en Python.
#ejemplo:
def decorador(funcion):
    def nueva_funcion():
        print("Antes de ejecutar la funcion")
        funcion()
        print("Despues de ejecutar la funcion")
        return nueva_funcion
@decorador
def saludar():
    print("Hola!")

# Ejercicio 3, Define a call function before map, filter or reduce, see examples.
print("Ejercicio 3:")
print("Ejemplo de uso de call function antes de map, filter o reduce:")
#map:
#ejemplo:
names = ['Sandra', 'Aaron', 'Sofia', 'Janize', 'Vanessa']  

def change_to_upper(name):
    return name.upper()
names_upper_cased = map(change_to_upper, names)
print("El ejemplo que se uso con map es:", list(names_upper_cased))
#en este ejemplo hicimos que imprimiera la lista de nombres en mayusculas.
#en este caso usamos la funcion change_to_upper antes de map para cambiar los nombres a mayusculas.

print("Ejemplo de uso de la funcion filter:")
#filter:
#ejemplo:
def starts_with_s(name):
        return name.lower().startswith('s')
names_inicia_con_s = filter(starts_with_s, names)
print("El ejemplo que se uso con filter es:", list(names_inicia_con_s))
#en este ejemplo hicimos que imprimiera el nombre o nombres que iniciaran con la letra "S".

print("Ejemplo de uso de funcion reduce:")
#reduce:
#ejemplo:
numbers_str = ['10', '20', '30', '40', '50']  
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print("El ejemplo que se uso con reduce es:", total)
#en este ejemplo hicimos que se sumaran todos los numeros de la lista numbers_str y nos devolviera el total.

# Ejercicio 4, Use for loop to print each country in the countries list.
print("Ejercicio 4:")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
for country in countries:
    print("Los paises en esta lista son:", country)

# Ejercicio 5, Use for to print each name in the names list.
print("Ejercicio 5:")
names = ['Sandra', 'Aaron', 'Sofia', 'Janize', 'Vanessa']
for name in names:
    print("Los nombres en esta lista son:", name)

# Ejercicio 6, Use for to print each number in the numbers list.
print("Ejercicio 6:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print("Los numeros en esta lista son:", number)


# Ejercicios de Nivel 2
print("Ejercicios de Nivel 2:")

# Ejercicio 1, Use map to create a new list by changing each country to uppercase in the countries list
print("Ejercicio 1:")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
countries_upper = map(lambda country: country.upper(), countries)
print("Los paises en mayusculas son:", list(countries_upper))

# Ejercicio 2, Use map to create a new list by changing each number to its square in the numbers list
print("Ejercicio 2:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_squared = map(lambda number: number ** 2, numbers)
print("Los numeros al cuadrado son:", list(numbers_squared))

# Ejercicio 3, Use map to change each name to uppercase in the names list
print("Ejercicio 3:")
names = ['Sandra', 'Aaron', 'Sofia', 'Janize', 'Vanessa']
names_upper = map(lambda name: name.upper(), names)
print("Los nombres en mayusculas son:", list(names_upper))

# Ejercicio 4, Use filter to filter out countries containing 'land'.
print("Ejercicio 4:")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
countries_with_land = filter(lambda country: 'land' in country, countries)
print("Los paises que contienen 'land' son:", list(countries_with_land))

# Ejercicio 5, Use filter to filter out countries having exactly six characters.
print("Ejercicio 5:")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
countries_with_six_characters = filter(lambda country: len(country) == 6, countries)
print("Los paises que tienen seis caracteres son:", list(countries_with_six_characters))

# Ejercicio 6, Use filter to filter out countries containing six letters and more in the country list.
print("Ejercicio 6:")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
countries_with_six_letters_or_more = filter(lambda country: len(country) >= 6, countries)
print("Los paises que tienen seis letras o mas son:", list(countries_with_six_letters_or_more))

# Ejercicio 7, Use filter to filter out country starting with 'E'.
print("Ejercicio 7:")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
countries_starting_with_e = filter(lambda country: country.startswith('E'), countries)
print("Los paises que empiezan con 'E' son o es:", list(countries_starting_with_e))

# Ejercicio 8, Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
print("Ejercicio 8:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = reduce(
    lambda x, y: x + y,  
    filter(
        lambda x: x % 2 == 0,  
        map(
            lambda x: x ** 2,  
            numbers
        )
    )
)
print("El resultado de encadenar map, filter y reduce es:", resultado)

# Ejercicio 9, Declare a function called get_string_lists which takes a list as a parameter 
#and then returns a list containing only string items.
print("Ejercicio 9:")
def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))
mixed_list = [1, 'hello', 3.14, 'world', True, 'Python']
string_list = get_string_lists(mixed_list)
print("La lista de solo strings es:", string_list)

# Ejercicio 10, Use reduce to sum all the numbers in the numbers list.
print("Ejercicio 10:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total_sum = reduce(lambda x, y: x + y, numbers)
print("La suma de todos los numeros es:", total_sum)

# Ejercicio 11, Use reduce to concatenate all the countries and to produce this sentence. 
#Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
print("Ejercicio 11:")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
sentence = reduce(
    lambda x, y: f"{x}, {y}" if y != countries[-1] else f"{x}, and {y}",
    countries) + " No son paises Europeos."
print(sentence)

# Ejercicio 12, Declare a function called categorize_countries that returns a list of countries with some common pattern.
#(you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
print("Ejercicio 12: ")
def categorize_countries(pattern):
    return list(filter(lambda country: pattern in country, countries))
pattern = 'land'
categorized_countries = categorize_countries(pattern)
print(f"Los paises que contienen '{pattern}' son:", categorized_countries)

# Ejercicio 13, Create a function returning a dictionary, where keys stand for starting letters of countries.
#and values are the number of country names starting with that letter.
print("Ejercicio 13:")
def count_countries_by_letter(countries):
    country_count = {}
    for country in countries:
        first_letter = country[0].upper()
        country_count[first_letter] = country_count.get(first_letter, 0) + 1
    return country_count
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
country_count_by_letter = count_countries_by_letter(countries)
print("El conteo de paises por letra inicial es:", country_count_by_letter)

# Ejercicio 14, Declare a get_first_ten_countries function.
#it returns a list of first ten countries from the countries.js list in the data folder.
print("Ejercicio 14:")
import countries_data as c 
countries = c.countries_data
def get_first_ten_countries(lst):
     return lst[:10]
print("Los primeros 10 paises son:", get_first_ten_countries(countries))

# Ejercicio 15, Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
print("Ejercicio 15:")
import countries_data as c 
countries = c.countries_data
def get_last_ten_countries(lst):
     return lst[-10:]
print("Los ultimos 10 paises son:", get_last_ten_countries(countries))

##Ejercicios de Nivel 3
print("Ejercicios de Nivel 3:")

# Ejercicio 1, Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py).
#file and follow the tasks below:
print("Ejercicio 1:")
import countries_data as cd
paises = cd.countries_data

## Ejercicio 3.1, Sort countries by name, by capital, by population.
print("Ejercicio 3.1:")

#ordenar por nombre: 
sortedByName = sorted(paises, key = lambda x: x["name"])
for country in sortedByName:
     print(country["name"])
 
 # Ordenar por capital:
print("Por capital:")
sortedByCapital = sorted(paises, key = lambda x: x["capital"])
for country in sortedByCapital:
     print(country["capital"])
 
 # Ordenar por población:
print("Por población")
sortedByPopulation = sorted(paises, key = lambda x: x["population"])
for country in sortedByPopulation:
     print(country['name'] , "Población:" , country['population'])

## Ejercicio 3.2, Sort out the ten most spoken languages by location.
print("Ejercicio 3.2:")
sortedLanguages = sorted(paises, key=lambda x: x["population"], reverse = True)
print("Los 10 idiomas más hablados por ubicación:")
top10Spoken = sortedLanguages[:10]
for language in top10Spoken:
     print(language['languages'] , ({language['name']}) , "cuantos lo hablan:" ,  language['population'] , " total de habitantes")

## Ejercicio 3.3, Sort out the ten most populated countries.
print("Ejercicio 3.3:")
sorted_countries = sorted(paises, key=lambda x: x["population"], reverse=True)
top_10_populated = sorted_countries[:10]
print("Los 10 países más poblados son estos:")
for country in top_10_populated:
     print(country["name"]) , country["population"]

#END OF DAY-14

print("revisado")