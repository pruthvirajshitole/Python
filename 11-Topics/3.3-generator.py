'''
Generator Function in Python
    - A generator function is a special type of function that returns an iterator object.
    - Instead of using return to send back a single value, generator functions use yield
      to produce a series of results over time.
    - This allows the function to generate values and pause its execution after each yield,
      maintaining its state between iterations.
    
Creating a Generator:
    - In Python, you can create a generator by using the yield statement in a function.
    - The yield statement returns a value from the generator and suspends the execution
      of the function until the next value is requested.

- Generators in Python are a powerful tool for working with large or complex data sets,
  allowing you to generate the values on-the-fly and store only what you need in memory.
- Whether you are working with a large dataset, performing complex calculations,
  or generating a sequence of values, generators are a must-have tool in your programming toolkit.

'''
print('------generator------')
def my_gen(max):
    count = 1
    while count <= max:
        yield count
        count += 1

count = my_gen(4)
for n in count:
    print(n)
    
l = list(count)
print(l)


print('-----Ex------')
# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def fun():
    yield 1            
    yield 2            
    yield 3            
 
# Driver code to check above generator function
for val in fun(): 
    print(val)

print('----simple generator------')

def my_generator():
    for i in range(5):
        yield i

gen = my_generator()
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
print(next(gen))  # 4
# print(next(gen))  # StopIteration


'''
As you can see, the generator function my_generator() returns a generator object, which can be used
to generate the values in the range 0 to 4. The next() function is used to request the next value from
the generator, and the generator resumes its execution until it encounters another yield statement
or until it reaches the end of the function.

'''

