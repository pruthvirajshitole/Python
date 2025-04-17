'''
Data Types: / Data Structures / Collections
   used to classify data items,
   identify thier size,
   and determine what can be done with them
Text Type       :  str   ("abc123")
Numeric Type    :  int(0,1,2,-6,-8,999),
                   float(12.57,13.876543,-15.87654),
                   complex(3+5j,-4+2j) 
Sequence Type   :  list,tuple,range
Mapping Type    :  dict
Set Type        :  set,frozenset
Boolean Type    :  bool (True , False)
Null Type       :  None
'''



'''
Data types | Heterogenous  |   Indexed |    Ordered |    Mutable |    Unique |    Brackets

----------------------------------------------------------------------------------------------

List       |    y          |   y       |    y       |     y      |     n      |     []

----------------------------------------------------------------------------------------------

Tuple      |    y          |   y       |    y       |     n      |     n      |     ()

----------------------------------------------------------------------------------------------

Set        |    y          |   n       |     n      |      y      |     y     |     {}

----------------------------------------------------------------------------------------------

Dictionary |    y (values) |   y (keys)|    y       |     y      | n(values), y(keys)|    {}
----------------------------------------------------------------------------------------------

String     |    y          |      y    |    y       |     n       |   n        |    ('',"",''' ''', """ """)
'''

'''
list :
    Sequence Type:
    collection of hetrogenous(different type) data,
    indexed and ordered,
    mutable(changes),
    allows duplicate values,
    elements written in square brackets[],
    
    - Mutation:
      append()
      extend()
      insert()
      update()

    - Delete:
      remove()
      pop()
      clear()
      del

    - Operation:
      concatenate (+)
      product (*)


tuple :
   Sequence Type:
    collection of hetrogenous(different type) data,
    indexed and ordered,
    immutable(changes not possible),
    allows duplicate values,
    elements written in round brackets()

   del


set :
    Sequence Type:
    collection of hetrogenous(different type) data,
    unindexed and unordered,
    mutable(changes),
    duplicate values not allowed (unique values),
    elements written in curly brackets{}

    - Mutation:
      add()
      update()

    - Delete:
      remove()
      discard()
      pop()
      clear()
      del

    - Operations:
      union (|)
      intersection (&)
      intersection_update()
      difference()
      symmetric_difference()

    - Methods:
      isdisjoint()
      issubset()
      issuperset()

dictionary:
    Mapping Type:    
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


string: 
  Sequence Type:
      collection of hetrogenous(different type) data,
      indexed and ordered,
      immutable(unchangable),
      allows duplicate values,
      elements written in (' '," ",''' ''',""" """)

      upper()
      lower()
      strip()
      replace()
      split()
      join()
      format()

    escape characters: 
      \' , \"
      \n  new line
      \r  carriage return
      \t  tab
      \b  backspace

'''