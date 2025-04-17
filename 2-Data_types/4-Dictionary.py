'''
Mapping Type:
Dictionary:

    collection of hetrogenous(different type) data,
    indexed(keys are the indexes) and ordered,
    mutable(changes are possible),
    allows duplicate values but keys are unique,
    elements are key-value pairs,
    elements written in curly brackets{}

    - functions:
      .get()
      .keys()
      .values()
      .items()

    - Mutation:
      .update()   

    - Delete:
      .pop('key')
      .popitem()
      .clear()
      del
'''

print('--------------dictionary-----------------')

d = {'Name':'Pruthviraj', 'Age':20, 'City':'Pune', 'Country':'India'}
print(d)
# Name is key and Pruthviraj is value
# Both keys and values combinly one element

print('---------duplicate keys are not allowed-----------')
d = {'Name':'Pruthviraj', 'Age':20, 'City':'Pune', 'Country':'India', 'Name':'Jordy'} 
print(d)
print(type(d))   # <class 'dict'>

print(len(d))  # len()

car = {'brand':'Ford', 'model':'Mustang', 'year':1990, 'color':['red', 'green', 'red', 'black', 'blue', 'red']}
print(car)


# Slicing

print('---------Slicing with keys-----------')

print(car['brand'])
print(car['model'])
print(car['year'])

# I love Ford of black color
print(f''' I love {car['brand']} of {car['color'][2]} color''')

# Ford is available in ['green', 'red', 'blue', 'black'] colors from 1990
print(f'''{car['brand']} is available in {list(set(car['color']))} colors from {car['year']}.''')

print(car.get('brand'))  
print(car.keys())       # all keys
print(car.values())     # all values
print(car.items())      # all (key,value)


# 1-Changes in dictionary

print('------------update()--------------')

car = {'brand':'Ford', 'model':'Mustang', 'year':1990, 'color':['red', 'green', 'red', 'black', 'blue', 'red']}

car['year'] = 2000
print(car)

car.update({'year':2010,'brand':'ferrari'})  # we can pass one or more key-value pairs
print(car)

# 2-Add a new pair

print('------------adding a new pair--------------')

car['price'] = 20000000
print(car)

car.update({'type':'auto driving'})
print(car)


# 3-Remove dictionary items

print('------------pop()--------------')

car.pop('year')
print(car)

print('------------popitem()--------------')

car.popitem()  # removes last item
print(car)

print('------------del key--------------')

del car['price']
print(car)

print('------------clear()--------------')

car.clear()
print(car)  # {} empty dictionary
print(type(car))

print('------------del--------------')

del car  # permanantly deletes the dictionary
# print(car)  # NameError: name 'car' is not defined.

l=[1,2,3,5,[11,"Steve",78] ,(('Apple'),'Microsoft'),{"founder":['Woz','Jobs'],"year":1980}]
# Steve Woz is one of the founder of Apple in 1980.

print(l[4][1],l[6]['founder'][0],"is one of the founder of",l[5][0],"in",l[-1]['year'],".") 