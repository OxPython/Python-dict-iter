'''
Created on Jul 2, 2014

@author: viejoemer

HowTo create an iterator from a dict in python?

¿Cómo crear un iterador de un diccionario?

'''

#Creating a dict with data
d = {
     "red":100,
     "yellow":200,
     "blue" : 300
     }
print(d)

#Create a iterator of keys
#iter(d) is similar to iter(d.keys())
d2 = iter(d)
print(d2)

for i in d2:
    print(i)

#Create a iterator of values
d2 = iter(d.values())
print(d2)

for i in d2:
    print(i)


