##Ejercicios Nivel 1
print("Ejercicios Nivel 1:")

# Ejercicio 1, Declare an empty list.
print("Ejercicio 1:")
mi_list = [] #No tiene nada mi lista.
print(len(mi_list))

# Ejercicio 2, Declare a list with more than 5 items
print("Ejercicio 2:")
lista_de_frutas = ['Fresa', 'Guayaba','Kiwi', 'Mandarina', 'Sandia', 'Manzana','Pera', 'Mango']
print("lista_de_frutas:", lista_de_frutas)

# Ejercicio 3, Find the length of your list.
print("Ejercicio 3:")
print("Ejercicio 2:")
lista_de_frutas = ['Fresa', 'Guayaba','Kiwi', 'Mandarina', 'Sandia', 'Manzana','Pera', 'Mango']
print("lista_de_frutas:", lista_de_frutas)
longitud_lista = len(lista_de_frutas)
print("La longitud de la lista es:", longitud_lista)

# Ejercicio 4, Get the first item, the middle item and the last item of the list.
print("Ejercicio 4:")
lista_de_frutas = ['Fresa', 'Guayaba','Kiwi', 'Mandarina', 'Sandia', 'Manzana','Pera', 'Mango']
primer_item = lista_de_frutas[0]
mitad_item = lista_de_frutas[len(lista_de_frutas) // 2]
ultimo_item = lista_de_frutas[-1]
print("Primer item:", primer_item)
print("mitad item:", mitad_item)
print("ultimo item:", ultimo_item)

# Ejercicio 5, Declare a list called mixed_data_types, put your.
# (name, age, height, marital status, address)
print("Ejercicio 5:")
mixed_data_types_lista=['Sandra', '18', '50 kg', 'soltera', 'Av. Paseos de la Asuncion 5300 int. 89']
print(mixed_data_types_lista)

# Ejercicio 6, Declare a list variable named it_companies and assign initial values.
# Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
print("Ejercicio 6:")
it_companies_lista= ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print('it_companies_lista:', it_companies_lista)
print('Numero de compañias:',len(it_companies_lista))

# Ejercicio 7, Print the list using print().
print("Ejercicio 7:")
it_companies_lista = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies_lista)

# Ejercicio 8, Print the number of companies in the list.
print("Ejercicio 8:")
print('Numero de compañias:',len(it_companies_lista))

# Ejercicio 9, Print the first, middle and last company.
print("Ejercicio 9:")
it_companies_lista = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
primer_item = it_companies_lista[0]
mitad_item = it_companies_lista[len(it_companies_lista) // 2]
ultimo_item = it_companies_lista[-1]
print("Primer item:", primer_item)
print("mitad item:", mitad_item)
print("ultimo item:", ultimo_item)

# Ejercicio 10, Print the list after modifying one of the companies.
print("Ejercicio 10:")
it_companies_lista = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies_lista[0] = 'Instagram'
print(it_companies_lista)

# Ejercicio 11, Add an IT company to it_companies.
print("Ejercicio 11:")
it_companies_lista=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies_lista.append('Tiktok')
print(it_companies_lista)

# Ejercicio 12, Insert an IT company in the middle of the companies list.
print("Ejercicio 12:")
it_companies_lista= ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
middle_index = len(it_companies_lista) // 2
it_companies_lista.insert(middle_index, 'Netflix')
print(it_companies_lista)

# Ejercicio 13, Change one of the it_companies names to uppercase (IBM excluded!).
print("Ejercicio 13:")
it_companies_lista= ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies_lista[0]= it_companies_lista[0].upper()
it_companies_lista[1]= it_companies_lista[1].upper()
it_companies_lista[2]= it_companies_lista[2].upper()
it_companies_lista[3]= it_companies_lista[3].upper()
it_companies_lista[4]= it_companies_lista[4].upper()
it_companies_lista[5]= it_companies_lista[5].upper()
it_companies_lista[6]= it_companies_lista[6].upper()
print(it_companies_lista)

# Ejercicio 14, Join the it_companies with a string '#;  '
print("Ejercicio 14:")
it_companies_lista = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
unir_companies = '#; '.join(it_companies_lista)
print(unir_companies)

# Ejercicio 15, Check if a certain company exists in the it_companies list.
print("Ejercicio 15:")
it_companies_lista= ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
does_exist = 'WhatsApp' in it_companies_lista
print(does_exist)  
does_exist = 'Apple' in it_companies_lista
print(does_exist)

# Ejercicio 16, Sort the list using sort() method.
print("Ejercicio 16:")
it_companies_lista = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies_lista.sort()
print(it_companies_lista)

# Ejercicio 17, Reverse the list in descending order using reverse() method.
print("Ejercicio 17:")
it_companies_lista = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies_lista.reverse()
print(it_companies_lista)

# Ejercicio 18, Slice out the first 3 companies from the list.
print("Ejercicio 18:")
it_companies_lista = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
primeras_tres_companies= it_companies_lista[:3]
print(primeras_tres_companies)

# Ejercicio 19, Slice out the last 3 companies from the list.
print("Ejercicio 19:")
it_companies_lista = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
ultimas_tres_companies = it_companies_lista[-3:]
print(ultimas_tres_companies)

# Ejercicio 20, Slice out the middle IT company or companies from the list.
print("Ejercicio 20:")
it_companies_lista=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
length = len(it_companies_lista)
middle = length // 2
nueva_lista = it_companies_lista[:middle-1] + it_companies_lista[middle+1:] if length % 2 == 0 else it_companies_lista[:middle] + it_companies_lista[middle+1:]
print(nueva_lista)

# Ejercicio 21, Remove the first IT company from the list.
print("Ejercicio 21:")
it_companies_lista = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
nueva_lista = it_companies_lista[1:]
print(nueva_lista)

# Ejercicio 22, Remove the middle IT company or companies from the list.
print("Ejercicio 22:")
it_companies_lista = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
length = len(it_companies_lista)
middle = length // 2 
nueva_lista = it_companies_lista[:middle-1]
print(nueva_lista)

# Ejercicio 23, Remove the last IT company from the list.
print("Ejercicio 23:")
it_companies_lista = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
nueva_lista = it_companies_lista[:-1]
print(nueva_lista)

# Ejercicio 24, Remove all IT companies from the list.
print("Ejercicio 24:")
it_companies_lista = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
nueva_lista = []
print(nueva_lista)

# Ejercicio 25, Destroy the IT companies list.
print("Ejercicio 25:")
it_companies_lista = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
del it_companies_lista
print("La lista ha sido destruida")


# Ejercicio 26, Join the following lists.
print("Ejercicio 26:")
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full = front_end + back_end
print(full)

# Ejercicio 27, After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack.
#then insert Python and SQL after Redux.
print("Ejercicio 27:")
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full = front_end + back_end
insert_index = full.index('Redux') + 1
full[insert_index:insert_index] = ['Python', 'SQL']
print(full)

##Ejercicios Nivel 2
print("Ejercicios de nivel 2:")

# Ejercicio 1, The following is a list of 10 students ages.
print("Ejercicio 28:")
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
 

# Ejercicio 2, Sort the list and find the min and max age.
print("Ejercicio 2:")
ages.sort()
print(ages)
print(ages[0], "," ,ages[len(ages)-1])

# Ejercicio 3, Add the min age and the max age again to the list.
print("Ejercicio 3:")
ages.insert(0, 19)
ages.insert(-1, 26)
print(ages)

# Ejercicio 4, Find the median age (one middle item or two middle items divided by two).
print("Ejercicio 4:")
age_media = (ages[5] + ages[6]) / 2
print("L a edad media es:", age_media)

# Ejercicio 5, Find the average age (sum of all items divided by their number).
print("Ejercicio 5:")
average = sum(ages) / len(ages)
print("El rango en las edades es de:", average)

# Ejercicio 6, Find the range of the ages (max minus min).
print("Ejercicio 6:")
range = ages[-1] - ages[0]
print("El rango de las edades es:", range)

# Ejercicio 7, Compare the value of (min - average) and (max - average), use abs() method.
print("Ejercicio 7:")
min = abs(ages[0] - average)
max = abs(ages[-1] - average)
print(min)
print(max)
comparacion = (min and max)
print("El resultado de esta comparacion es:", comparacion)

# Ejercicio 8, Find the middle country(ies) in the countries list.
print("Ejercicio 8:")
import countries as p
print(len(p.countries))
media = int(len(p.countries)/2)
print(media)
print(p.countries[(media)]+ " , "+p.countries[(media+1)])
if 'Mexico' in p.countries:
    print('Mexico esta en :', p.countries.index('Mexico'))
else:
    print('No esta')
print(p.countries.index('Mexico'))
print('Mexico' in p.countries)

# Ejercicio 9, Divide the countries list into two equal lists if it is even if not one more country for the first half.
print("Ejercicio 9:")
print(int(len(p.countries)/2))
lista_uno = p.countries[0:96]
print("La lista uno es:", lista_uno)
print(len(lista_uno))
lista_dos = p.countries[96:193]
print( "La lista dos es:",lista_dos)
print(len(lista_dos))

# Ejercicio 10, ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. 
#Unpack the first three countries and the rest as scandic countries.
print("Ejercicio 10:")
Countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print("Los primeros tres countries son:", Countries[:3])
print( "Los Scandic countries son:", Countries [3:])

#END OF DAY-5