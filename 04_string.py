#Digita tu información:

name=input('Cuál es tu nombre?')
last_name=input('Cuál es tu apellido?')
my_age=input('Cuál es tu edad?')

full_name= f'{name} {last_name}'
print(full_name)

Complete= f'{name} {last_name} {my_age}'
print(Complete)

#format
template= 'Hola, mi nombre es ' + name + ', mi apellido es ' + last_name + ' y mi edad es ' + my_age
print("v1", " " , template)

template= 'Hola, mi nombre es {}, mi apellido es {} y mi edad es {}'.format(name , last_name, my_age)
print("v2", " " , template)

template= f'Hola, mi nombre es {name}, mi apellido es {last_name} y mi edad es {my_age}'
print("v3", " " ,template)



'''
quote="I'm Nicolas"
print(quote)

quote2 = 'She said "Hello" '
print(quote2)

'''