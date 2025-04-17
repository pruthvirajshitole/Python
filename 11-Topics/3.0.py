"""
+---------------------------------------------------------------------------------------------------------+
| Feature        | Iterator                   | Generator                   | Decorator                   |
|----------------+----------------------------+-----------------------------+-----------------------------|
| Definition     | An object that allows      | A special type of iterator  | A function that modifies    |
|                | sequential access to       | created using a function    | the behavior of another     |
|                | elements in a collection.  | with 'yield' keyword.       | function or method.         |
|----------------+----------------------------+-----------------------------+-----------------------------|
| Creation       | Implemented using          | Defined using a function    | Defined using '@' syntax    |
|                | __iter__() and __next__()  | with 'yield' keyword.       | or as a higher-order        |
|                | methods.                   |                             | function.                   |
|----------------+----------------------------+-----------------------------+-----------------------------|
| Memory Usage   | May require more memory    | More memory-efficient as    | No direct impact on memory. |
|                | as all elements are stored.| values are generated lazily.|                             |
|----------------+----------------------------+-----------------------------+-----------------------------|
| Use Case       | Iterating over collections | Generating large sequences  | Modifying or extending      |
|                | like lists, tuples, etc.   | lazily without storing them.| function behavior.          |
|----------------+----------------------------+-----------------------------+-----------------------------|
| Example:       |                            |                             |                             |
| (Code)         | class MyIterator:          | def my_generator():         | @my_decorator               |
|                |     def __iter__(self):    |     for i in range(5):      | def my_function():          |
|                |         return self        |         yield i             |     pass                    |
|                |     def __next__(self):    |                             |                             |
|                |         # Logic here       |                             |                             |
+---------------------------------------------------------------------------------------------------------+
"""