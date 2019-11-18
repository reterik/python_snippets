#------------------------------------------------------------------------------------------#
#    Python 3.6 Snippets
#
#    Copyright 2019 Googlier LLC - Joseph Hettich
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#Also add information on how to contact you by electronic and paper mail.
#If the program does terminal interaction, make it output a short notice like this when it starts in an interactive mode:
#------------------------------------------------------------------------------------------#

print("Copyright 2019 Googlier LLC - Joseph Hettich "+
"This program comes with ABSOLUTELY NO WARRANTY; "+
"This is free software, and you are welcome to redistribute it " +
"under certain conditions;")

def all_unique(lst):
  return len(lst) == len(set(lst))
  
x = [1,2,3,4,5,6]
y = [1,2,2,3,4,5]
t = all_unique(x) # True
s = all_unique(y) # False

print(s)
print(t)

#------------------------------------------------------------------------------------------#
#all_unique
#Returns True if all the values in a flat list are unique, False otherwise.
#Use set() on the given list to remove duplicates, compare its length with the length of the list.
#------------------------------------------------------------------------------------------#

def all_equal(lst):
  return lst[1:] == lst[:-1]

t = all_equal([1, 2, 3, 4, 5, 6]) # False
s = all_equal([1, 1, 1, 1]) # True

print(s)
print(t)

#------------------------------------------------------------------------------------------#
#bifurcate_by
#Splits values into two groups according to a function, which specifies which group an element in the input list belongs to. If the function returns True, the element belongs to the first group; otherwise, it belongs to the second group.
#Use list comprehension to add elements to groups, based on fn.
#------------------------------------------------------------------------------------------#

def bifurcate(lst, filter):
  return [
    [x for i,x in enumerate(lst) if filter[i] == True],
    [x for i,x in enumerate(lst) if filter[i] == False]
  ]

t = bifurcate(['beep', 'boop', 'foo', 'bar'], [True, True, False, True]) # [ ['beep', 'boop', 'bar'], ['foo'] ]

print(t)

#------------------------------------------------------------------------------------------#
#chunk
#Chunks a list into smaller lists of a specified size.
#Use list() and range() to create a list of the desired size. Use map() on the list and fill it with splices of the given list. Finally, return use created list.
#------------------------------------------------------------------------------------------#

from math import ceil

def chunk(lst, size):
  return list(
    map(lambda x: lst[x * size:x * size + size],
      list(range(0, ceil(len(lst) / size)))))

t = chunk([1,2,3,4,5],2) # [[1,2],[3,4],5]

print(t)

#------------------------------------------------------------------------------------------#
#compact
#Removes falsey values from a list.
#Use filter() to filter out falsey values (False, None, 0, and "").
#------------------------------------------------------------------------------------------#

def compact(lst):
  return list(filter(bool, lst))

t = compact([0, 1, False, 2, '', 3, 'a', 's', 34]) # [ 1, 2, 3, 'a', 's', 34 ]

print(t)

#------------------------------------------------------------------------------------------#
#count_by
#Groups the elements of a list based on the given function and returns the count of elements in each group.
#Use map() to map the values of the given list using the given function. Iterate over the map and increase the element count each time it occurs.
#------------------------------------------------------------------------------------------#

def count_by(arr, fn=lambda x: x):
  key = {}
  for el in map(fn, arr):
    key[el] = 1 if el not in key else key[el] + 1
  return key

from math import floor
count_by([6.1, 4.2, 6.3], floor) # {6: 2, 4: 1}
count_by(['one', 'two', 'three'], len) # {3: 2, 5: 1}

#------------------------------------------------------------------------------------------#
#count_occurences
#Counts the occurrences of a value in a list.
#Increment a counter for every item in the list that has the given value and is of the same type.
#------------------------------------------------------------------------------------------#

def count_occurrences(lst, val):
  return len([x for x in lst if x == val and type(x) == type(val)])

t = count_occurrences([1, 1, 2, 1, 2, 3], 1) # 3

print(t)

#------------------------------------------------------------------------------------------#
#deep_flatten
#Deep flattens a list.
#Use recursion. Define a function, spread, that uses either list.extend() or list.append() on each element in a list to flatten it. Use list.extend() with an empty list and the spread function to flatten a list. Recursively flatten each element that is a list.
#------------------------------------------------------------------------------------------#

def spread(arg):
  ret = []
  for i in arg:
    if isinstance(i, list):
      ret.extend(i)
    else:
      ret.append(i)
  return ret

def deep_flatten(lst):
  result = []
  result.extend(
    spread(list(map(lambda x: deep_flatten(x) if type(x) == list else x, lst))))
  return result

t = deep_flatten([1, [2], [[3], 4], 5]) # [1,2,3,4,5]

print(t)

#------------------------------------------------------------------------------------------#
#difference_by
#Returns the difference between two lists, after applying the provided function to each list element of both.
#Create a set by applying fn to each element in b, then use list comprehension in combination with fn on a to only keep values not contained in the previously created set, _b.
#------------------------------------------------------------------------------------------#

def difference_by(a, b, fn):
  _b = set(map(fn, b))
  return [item for item in a if fn(item) not in _b]

from math import floor
difference_by([2.1, 1.2], [2.3, 3.4],floor) # [1.2]
t = difference_by([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], lambda v : v['x']) # [ { x: 2 } ]

print(t)

#------------------------------------------------------------------------------------------#
#every
#Returns True if the provided function returns True for every element in the list, False otherwise.
#Use all() in combination with map and fn to check if fn returns True for all elements in the list.
#------------------------------------------------------------------------------------------#

def every(lst, fn=lambda x: x):
  return all(map(fn, lst))

every([4, 2, 3], lambda x: x > 1) # True
t = every([1, 2, 3]) # True

print(t)

#------------------------------------------------------------------------------------------#
#every_nth
#Returns every nth element in a list.
#Use [nth-1::nth] to create a new list that contains every nth element of the given list.
#------------------------------------------------------------------------------------------#

def every_nth(lst, nth):
  return lst[nth-1::nth]

every_nth([1, 2, 3, 4, 5, 6], 2) # [ 2, 4, 6 ]

#------------------------------------------------------------------------------------------#
#filter_non_unique
#Filters out the non-unique values in a list.
#Use list comprehension and list.count() to create a list containing only the unique values.
#------------------------------------------------------------------------------------------#

def filter_non_unique(lst):
  return [item for item in lst if lst.count(item) == 1]

t = filter_non_unique([1, 2, 2, 3, 4, 4, 5]) # [1, 3, 5]

print(t)

#------------------------------------------------------------------------------------------#
#filter_unique
#Filters out the unique values in a list.
#Use list comprehension and list.count() to create a list containing only the non-unique values.
#------------------------------------------------------------------------------------------#

def filter_unique(lst):
  return [x for x in set(item for item in lst if lst.count(item) > 1)]

t = filter_unique([1, 2, 2, 3, 4, 4, 5]) # [2, 4]

print(t)

#------------------------------------------------------------------------------------------#
#flatten
#Flattens a list of lists once.
#Use nested list comprehension to extract each value from sub-lists in order.
#------------------------------------------------------------------------------------------#

def flatten(lst):
  return [x for y in lst for x in y]

t = flatten([[1,2,3,4],[5,6,7,8]]) # [1, 2, 3, 4, 5, 6, 7, 8]

print(t)

#------------------------------------------------------------------------------------------#
#group_by
#Groups the elements of a list based on the given function.
#Use map() and fn to map the values of the list to the keys of an object. Use list #comprehension to map each element to the appropriate key.
#------------------------------------------------------------------------------------------#

def group_by(lst, fn):
    return {key : [el for el in lst if fn(el) == key] for key in map(fn,lst)}

import math
group_by([6.1, 4.2, 6.3], math.floor) # {4: [4.2], 6: [6.1, 6.3]}
t = group_by(['one', 'two', 'three'], len) # {3: ['one', 'two'], 5: ['three']}

print(t)

#------------------------------------------------------------------------------------------#
#has_duplicates
#Returns True if there are duplicate values in a flast list, False otherwise.
#Use set() on the given list to remove duplicates, compare its length with the length of the list.
#------------------------------------------------------------------------------------------#

def has_duplicates(lst):
  return len(lst) != len(set(lst))

x = [1,2,3,4,5,5]
y = [1,2,3,4,5]
s = has_duplicates(x) # True
t = has_duplicates(y) # False

print(s)
print(t)

#------------------------------------------------------------------------------------------#
#head
#Returns the head of a list.
#use lst[0] to return the first element of the passed list.
#------------------------------------------------------------------------------------------#

def head(lst):
  return lst[0]

t = head([1, 2, 3]); # 1

print(t)

#------------------------------------------------------------------------------------------#
#initial
#Returns all the elements of a list except the last one.
#Use lst[0:-1] to return all but the last element of the list.
#------------------------------------------------------------------------------------------#

def initial(lst):
  return lst[0:-1]

t = initial([1, 2, 3]); # [1,2]

print(t)

#------------------------------------------------------------------------------------------#
#initialize_2d_list
#Initializes a 2D list of given width and height and value.
#Use list comprehension and range() to generate h rows where each is a list with length h, initialized with val. If val is not provided, default to None.
#------------------------------------------------------------------------------------------#

def initialize_2d_list(w,h, val = None):
  return [[val for x in range(w)] for y in range(h)]

t = initialize_2d_list(2, 2, 0) # [[0,0], [0,0]]
print(t)

#------------------------------------------------------------------------------------------#
#initialize_list_with_range
#Initializes a list containing the numbers in the specified range where start and end are inclusive with their common difference step.
#Use list and range() to generate a list of the appropriate length, filled with the desired values in the given range. Omit start to use the default value of 0. Omit step to use the default value of 1.
#------------------------------------------------------------------------------------------#

def initialize_list_with_range(end, start = 0, step = 1):
  return list(range(start, end + 1, step))

initialize_list_with_range(5) # [0, 1, 2, 3, 4, 5]
initialize_list_with_range(7,3) # [3, 4, 5, 6, 7]
t = initialize_list_with_range(9,0,2) # [0, 2, 4, 6, 8]

print(t)

#------------------------------------------------------------------------------------------#
#initialize_list_with_values
#Initializes and fills a list with the specified value.
#Use list comprehension and range() to generate a list of length equal to n, filled with the desired values. Omit val to use the default value of 0.
#------------------------------------------------------------------------------------------#

def initialize_list_with_values(n, val = 0):
  return [val for x in range(n)]

t = initialize_list_with_values(5, 2) # [2, 2, 2, 2, 2]

print(t)

#------------------------------------------------------------------------------------------#
#intersection
#Returns a list of elements that exist in both lists.
#Create a set from a and b, then use the built-in set operator & to only keep values contained in both sets, then transform the set back into a list.
#------------------------------------------------------------------------------------------#

def intersection(a, b):
  _a, _b = set(a), set(b)
  return list(_a & _b)

t = intersection([1, 2, 3], [4, 3, 2]) # [2, 3]

print(t)

#------------------------------------------------------------------------------------------#
#intersection_by
#Returns a list of elements that exist in both lists, after applying the provided function to each list element of both.
#Create a set by applying fn to each element in b, then use list comprehension in combination with fn on a to only keep values contained in both lists.
#------------------------------------------------------------------------------------------#

def intersection_by(a, b, fn):
  _b = set(map(fn, b))
  return [item for item in a if fn(item) in _b]

from math import floor
t = intersection_by([2.1, 1.2], [2.3, 3.4],floor) # [2.1]

print(t)

#last
#Returns the last element in a list.
#use lst[-1] to return the last element of the passed list.

def last(lst):
  return lst[-1]

t = last([1, 2, 3]) # 3

print(t)

#------------------------------------------------------------------------------------------#
#longest_item
#Takes any number of iterable objects or objects with a length property and returns the longest one. If multiple objects have the same length, the first one will be returned.
#Use max() with len as the key to return the item with the greatest length.
#------------------------------------------------------------------------------------------#

def longest_item(*args):
  return max(args, key = len)

q = longest_item('this', 'is', 'a', 'testcase') # 'testcase'
s = longest_item([1, 2, 3], [1, 2], [1, 2, 3, 4, 5]) # [1, 2, 3, 4, 5]
t = longest_item([1, 2, 3], 'foobar') # 'foobar'

print(q)
print(s)
print(t)

#------------------------------------------------------------------------------------------#
#max_element_index
#Returns the pindex of the element with the maximum value in a list.
#Use max() and list.index() to get the maximum value in the list and return its index.
#------------------------------------------------------------------------------------------#

def max_element_index(arr):
  return arr.index(max(arr))

t = max_element_index([5, 8, 9, 7, 10, 3, 0]) # 4

print(t)


#------------------------------------------------------------------------------------------#
#max_n
#Returns the n maximum elements from the provided list. If n is greater than or equal to the provided list's length, then return the original list (sorted in descending order).=

#Use sorted() to sort the list, [:n] to get the specified number of elements. Omit the second argument, n, to get a one-element list.

#------------------------------------------------------------------------------------------#

def max_n(lst, n=1):
  return sorted(lst, reverse=True)[:n]

s = max_n([1, 2, 3]) # [3]
t = max_n([1, 2, 3], 2) # [3,2]

print(s)
print(t)


#------------------------------------------------------------------------------------------#
#min_n
#Returns the n minimum elements from the provided list. If n is greater than or equal to the provided list's length, then return the original list (sorted in ascending order).
#Use sorted() to sort the list, [:n]to get the specified number of elements. Omit the second argument,n`, to get a one-element list.
#------------------------------------------------------------------------------------------#

def min_n(lst, n=1):
  return sorted(lst, reverse=False)[:n]

t = min_n([1, 2, 3]) # [1]
s = min_n([1, 2, 3], 2) # [1,2]

print(s)
print(t)


#------------------------------------------------------------------------------------------#
#most_frequent
#Returns the most frequent element in a list.

#Use set(list) to get the unique values in the list combined with max() to find the element that has the most appearances.
#------------------------------------------------------------------------------------------#

def most_frequent(list):
  return max(set(list), key = list.count)

t = most_frequent([1,2,1,2,3,2,1,4,2]) #2

print(t)

#------------------------------------------------------------------------------------------#
#none
#Returns False if the provided function returns True for at least one element in the list, True otherwise.

#Use all() and fn to check if fn returns False for all the elements in the list.
#------------------------------------------------------------------------------------------#

def none(lst, fn=lambda x: x):
  return all(not fn(x) for x in lst)

s = none([0, 1, 2, 0], lambda x: x >= 2 ) # False
t = none([0, 0, 0]) # True

print(s)
print(t)

#------------------------------------------------------------------------------------------#
#offset
#Moves the specified amount of elements to the end of the list.

#Use lst[offset:] and lst[:offset] to get the two slices of the list and combine them before returning.
#------------------------------------------------------------------------------------------#

def offset(lst, offset):
  return lst[offset:] + lst[:offset]

s = offset([1, 2, 3, 4, 5], 2) # [3, 4, 5, 1, 2]
t = offset([1, 2, 3, 4, 5], -2) # [4, 5, 1, 2, 3]

print(s)
print(t)

#------------------------------------------------------------------------------------------#
#sample
#Returns a random element from an array.

#Use randint() to generate a random number that corresponds to an index in the list, return the element at that index.
#------------------------------------------------------------------------------------------#

from random import randint

def sample(lst):
  return lst[randint(0, len(lst) - 1)]

t = sample([3, 7, 9, 11]) # 9

print(t)

#------------------------------------------------------------------------------------------#
#shuffle
#Randomizes the order of the values of an list, returning a new list.

#Uses the Fisher-Yates algorithm to reorder the elements of the list.
#------------------------------------------------------------------------------------------#

from copy import deepcopy

def shuffle(lst):
  temp_lst = deepcopy(lst)
  m = len(temp_lst)
  while (m):
    m -= 1
    i = randint(0, m)
    temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]
  return temp_lst

foo = [1,2,3]
t = shuffle(foo) # [2,3,1] , foo = [1,2,3]

print(t)

#------------------------------------------------------------------------------------------#
#similarity
#Returns a list of elements that exist in both lists.

#Use list comprehension on a to only keep values contained in both lists.
#------------------------------------------------------------------------------------------#

def similarity(a, b):
  return [item for item in a if item in b]

similarity([1, 2, 3], [1, 2, 4]) # [1, 2]

#------------------------------------------------------------------------------------------#
#some
#Returns True if the provided function returns True for at least one element in the list, False otherwise.

#Use any() in combination with map() and fn to check if fn returns True for any element in the list.
#------------------------------------------------------------------------------------------#

def some(lst, fn=lambda x: x):
  return any(map(fn, lst))

some([0, 1, 2, 0], lambda x: x >= 2 ) # True
some([0, 0, 1, 0]) # True


#------------------------------------------------------------------------------------------#
#spread
#Flattens a list, by spreading its elements into a new list.

#Loop over elements, use list.extend() if the element is a list, list.append() otherwise.
#------------------------------------------------------------------------------------------#

def spread(arg):
  ret = []
  for i in arg:
    if isinstance(i, list):
      ret.extend(i)
    else:
      ret.append(i)
  return ret

spread([1,2,3,[4,5,6],[7],8,9]) # [1,2,3,4,5,6,7,8,9]


#------------------------------------------------------------------------------------------#
#symmetric_difference
#Returns the symmetric difference between two iterables, without filtering out duplicate values.

#Create a set from each list, then use list comprehension on each one to only keep values not contained in the previously created set of the other.
#------------------------------------------------------------------------------------------#

def symmetric_difference(a, b):
  _a, _b = set(a), set(b)
  return [item for item in a if item not in _b] + [item for item in b if item not in _a]

symmetric_difference([1, 2, 3], [1, 2, 4]) # [3, 4]

#------------------------------------------------------------------------------------------#
#symmetric_difference_by
#Returns the symmetric difference between two lists, after applying the provided function to each list element of both.

#Create a set by applying fn to each element in every list, then use list comprehension in combination with fn on each one to only keep values not contained in the previously created set of the other.
#------------------------------------------------------------------------------------------#

def symmetric_difference_by(a, b, fn):
  _a, _b = set(map(fn, a)), set(map(fn, b))
  return [item for item in a if fn(item) not in _b] + [item for item in b if fn(item) not in _a]

from math import floor
symmetric_difference_by([2.1, 1.2], [2.3, 3.4],floor) # [1.2, 3.4]

#------------------------------------------------------------------------------------------#
#tail
#Returns all elements in a list except for the first one.

#Return lst[1:] if the list's length is more than 1, otherwise, return the whole list.
#------------------------------------------------------------------------------------------#

def tail(lst):
  return lst[1:] if len(lst) > 1 else lst

tail([1, 2, 3]); # [2,3]
tail([1]); # [1]

#------------------------------------------------------------------------------------------#
#transpose
#Returns the transpose of a two-dimensional list.

#Use *lst to get the passed list as tuples. Use zip() in combination with list() to create the transpose of the given two-dimensional list.
#------------------------------------------------------------------------------------------#

def transpose(lst):
    return list(zip(*lst))

transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]) # [(1, 4, 7, 10), (2, 5, 8, 11), (3, 6, 9, 12)]

#------------------------------------------------------------------------------------------#
#union
#Returns every element that exists in any of the two lists once.

#Create a set with all values of a and b and convert to a list.
#------------------------------------------------------------------------------------------#

def union(a,b):
  return list(set(a + b))

union([1, 2, 3], [4, 3, 2]) # [1,2,3,4]

#------------------------------------------------------------------------------------------#
#union_by
#Returns every element that exists in any of the two lists once, after applying the provided function to each element of both.

#Create a set by applying fn to each element in a, then use list comprehension in combination with fn on b to only keep values not contained in the previously created set, _a. Finally, create a set from the previous result and a and transform it into a list
#------------------------------------------------------------------------------------------#

def union_by(a,b,fn):
  _a = set(map(fn, a))
  return list(set(a + [item for item in b if fn(item) not in _a]))

from math import floor
union_by([2.1], [1.2, 2.3], floor) # [2.1, 1.2]


'''------------------------------------------------------------------------------------------
unique_elements
Returns the unique elements in a given list.
Create a set from the list to discard duplicated values, then return a list from it.
------------------------------------------------------------------------------------------'''

def unique_elements(li):
  return list(set(li))

unique_elements([1, 2, 2, 3, 4, 3]) # [1, 2, 3, 4]



'''------------------------------------------------------------------------------------------
zip
Creates a list of elements, grouped based on the position in the original lists.

Use max combined with list comprehension to get the length of the longest list in the arguments. Loop for max_length times grouping elements. If lengths of lists vary, use fill_value (defaults to None).
------------------------------------------------------------------------------------------'''

def zip(*args, fill_value=None):
  max_length = max([len(lst) for lst in args])
  result = []
  for i in range(max_length):
    result.append([
      args[k][i] if i < len(args[k]) else fill_value for k in range(len(args))
    ])
  return result

zip(['a', 'b'], [1, 2], [True, False]) # [['a', 1, True], ['b', 2, False]]
zip(['a'], [1, 2], [True, False]) # [['a', 1, True], [None, 2, False]]
zip(['a'], [1, 2], [True, False], fill_value = '_') # [['a', 1, True], ['_', 2, False]]

'''------------------------------------------------------------------------------------------
Math
average
Returns the average of two or more numbers.

Use sum() to sum all of the args provided, divide by len(args).
------------------------------------------------------------------------------------------'''

def average(*args):
  return sum(args, 0.0) / len(args)

average(*[1, 2, 3]) # 2.0
average(1, 2, 3) # 2.0

'''------------------------------------------------------------------------------------------
average_by
Returns the average of a list, after mapping each element to a value using the provided function.

Use map() to map each element to the value returned by fn. Use sum() to sum all of the mapped values, divide by len(lst).
------------------------------------------------------------------------------------------'''

def average_by(lst, fn=lambda x: x):
  return sum(map(fn, lst), 0.0) / len(lst)

average_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda x: x['n']) # 5.0

'''------------------------------------------------------------------------------------------
clamp_number
Clamps num within the inclusive range specified by the boundary values a and b.

If num falls within the range, return num. Otherwise, return the nearest number in the range.
------------------------------------------------------------------------------------------'''

def clamp_number(num,a,b):
  return max(min(num, max(a,b)),min(a,b))

clamp_number(2, 3, 5) # 3
clamp_number(1, -1, -5) # -1

'''------------------------------------------------------------------------------------------

degrees_to_rads
Converts an angle from degrees to radians.

Use math.pi and the degrees to radians formula to convert the angle from degrees to radians.
------------------------------------------------------------------------------------------'''


import math

def degrees_to_rads(deg):
  return (deg * math.pi) / 180.0

degrees_to_rads(180) # 3.141592653589793


'''------------------------------------------------------------------------------------------
digitize
Converts a number to an array of digits.

Use map() combined with int on the string representation of n and return a list from the result.
------------------------------------------------------------------------------------------'''

def digitize(n):
  return list(map(int, str(n)))

digitize(123) # [1, 2, 3]

'''------------------------------------------------------------------------------------------
factorial
Calculates the factorial of a number.

Use recursion. If num is less than or equal to 1, return 1. Otherwise, return the product of num and the factorial of num - 1. Throws an exception if num is a negative or a floating point number.
------------------------------------------------------------------------------------------'''

def factorial(num):
  if not ((num >= 0) and (num % 1 == 0)):
    raise Exception(
      f"Number( {num} ) can't be floating point or negative ")
  return 1 if num == 0 else num * factorial(num - 1)

factorial(6) # 720

'''------------------------------------------------------------------------------------------
fibonacci
Generates an array, containing the Fibonacci sequence, up until the nth term.

Starting with 0 and 1, use list.append() to add the sum of the last two numbers of the list to the end of the list, until the length of the list reaches n. If nis less or equal to0, return a list containing 0`.
------------------------------------------------------------------------------------------'''

def fibonacci(n):
  if n <= 0:
    return [0]

  sequence = [0, 1]
  while len(sequence) <= n:
    next_value = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
    sequence.append(next_value)

  return sequence

t = fibonacci(1000) # [0, 1, 1, 2, 3, 5, 8, 13]

print(t)


'''------------------------------------------------------------------------------------------
gcd
Calculates the greatest common divisor of a list of numbers.

Use reduce() and math.gcd over the given list.
------------------------------------------------------------------------------------------'''

from functools import reduce
import math

def gcd(numbers):
  return reduce(math.gcd, numbers)

gcd([8,36,28]) # 4

'''------------------------------------------------------------------------------------------
in_range
Checks if the given number falls within the given range.

Use arithmetic comparison to check if the given number is in the specified range. If the second parameter, end, is not specified, the range is considered to be from 0 to start.
------------------------------------------------------------------------------------------'''

def in_range(n, start, end = 0):
  if (start > end):
    end, start = start, end
  return start <= n <= end

in_range(3, 2, 5); # True
in_range(3, 4); # True
in_range(2, 3, 5); # False
in_range(3, 2); # False


'''------------------------------------------------------------------------------------------
is_divisible
Checks if the first numeric argument is divisible by the second one.

Use the modulo operator (%) to check if the remainder is equal to 0.
------------------------------------------------------------------------------------------'''

def is_divisible(dividend, divisor):
  return dividend % divisor == 0

is_divisible(6, 3) # True

'''------------------------------------------------------------------------------------------
is_even
Returns True if the given number is even, False otherwise.

Checks whether a number is odd or even using the modulo (%) operator. Returns True if the number is even, False if the number is odd.
------------------------------------------------------------------------------------------'''

def is_even(num):
  return num % 2 == 0

is_even(3) # False

'''------------------------------------------------------------------------------------------
is_odd
Returns True if the given number is odd, False otherwise.

Checks whether a number is even or odd using the modulo (%) operator. Returns True if the number is odd, False if the number is even.
------------------------------------------------------------------------------------------'''

def is_odd(num):
  return num % 2 != 0

is_odd(3) # True

'''------------------------------------------------------------------------------------------
lcm advanced
Returns the least common multiple of two or more numbers.

Define a function, spread, that uses either list.extend() or list.append() on each element in a list to flatten it. Use math.gcd() and lcm(x,y) = x * y / gcd(x,y) to determine the least common multiple.
------------------------------------------------------------------------------------------'''

from functools import reduce
import math

def spread(arg):
  ret = []
  for i in arg:
    if isinstance(i, list):
      ret.extend(i)
    else:
      ret.append(i)
  return ret

def lcm(*args):
  numbers = []
  numbers.extend(spread(list(args)))

  def _lcm(x, y):
    return int(x * y / math.gcd(x, y))

  return reduce((lambda x, y: _lcm(x, y)), numbers)

lcm(12, 7) # 84
lcm([1, 3, 4], 5) # 60

'''------------------------------------------------------------------------------------------
max_by
Returns the maximum value of a list, after mapping each element to a value using the provided function.

Use map() with fn to map each element to a value using the provided function, use max() to return the maximum value.
------------------------------------------------------------------------------------------'''

def max_by(lst, fn):
  return max(map(fn,lst))

max_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 8

'''------------------------------------------------------------------------------------------
median
Finds the median of a list of numbers.

Sort the numbers of the list using list.sort() and find the median, which is either the middle element of the list if the list length is odd or the average of the two middle elements if the list length is even.
------------------------------------------------------------------------------------------'''

def median(list):
  list.sort()
  list_length = len(list)
  if list_length%2==0:
    return (list[int(list_length/2)-1] + list[int(list_length/2)])/2
  else:
    return list[int(list_length/2)]

median([1,2,3]) # 2
median([1,2,3,4]) # 2.5

'''-----------------------------------------------------------------------------------------
min_by
Returns the minimum value of a list, after mapping each element to a value using the provided function.

Use map() with fn to map each element to a value using the provided function, use min() to return the minimum value.
-----------------------------------------------------------------------------------------'''

def min_by(lst, fn):
  return min(map(fn,lst))

min_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 2

'''-----------------------------------------------------------------------------------------
rads_to_degrees
Converts an angle from radians to degrees.

Use math.pi and the radian to degree formula to convert the angle from radians to degrees.
-----------------------------------------------------------------------------------------'''

import math

def rads_to_degrees(rad):
  return (rad * 180.0) / math.pi

import math
rads_to_degrees(math.pi / 2) # 90.0

'''-----------------------------------------------------------------------------------------
sum_by
Returns the sum of a list, after mapping each element to a value using the provided function.

Use map() with fn to map each element to a value using the provided function, use sum() 
to return the sum of the values.
-----------------------------------------------------------------------------------------'''

def sum_by(lst, fn):
  return sum(map(fn,lst))

sum_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 20

'''-----------------------------------------------------------------------------------------
Object
keys_only
Returns a flat list of all the keys in a flat dictionary.

Use dict.keys() to return the keys in the given dictionary. Return a list() of the previous result.
-----------------------------------------------------------------------------------------'''

def keys_only(flat_dict):
  return list(flat_dict.keys())

ages = {
  "Peter": 10,
  "Isabel": 11,
  "Anna": 9,
}
keys_only(ages) # ['Peter', 'Isabel', 'Anna']

'''-----------------------------------------------------------------------------------------
map_values
Creates an object with the same keys as the provided object and values generated by running the provided function for each value.

Use dict.keys() to iterate over the object's keys, assigning the values produced by fn to each key of a new object.
-----------------------------------------------------------------------------------------'''

def map_values(obj, fn):
  ret = {}
  for key in obj.keys():
    ret[key] = fn(obj[key])
  return ret

users = {
  'fred': { 'user': 'fred', 'age': 40 },
  'pebbles': { 'user': 'pebbles', 'age': 1 }
}

map_values(users, lambda u : u['age']) # {'fred': 40, 'pebbles': 1}

'''-----------------------------------------------------------------------------------------
values_only
Returns a flat list of all the values in a flat dictionary.

Use dict.values() to return the values in the given dictionary. Return a list() of the previous result.
-----------------------------------------------------------------------------------------'''

def values_only(flat_dict):
  return list(flat_dict.values())

ages = {
  "Peter": 10,
  "Isabel": 11,
  "Anna": 9,
}
values_only(ages) # [10, 11, 9]

'''-----------------------------------------------------------------------------------------
String
byte_size
Returns the length of a string in bytes.

Use s.encode('utf-8') to encode the given string and return its length.
-----------------------------------------------------------------------------------------'''

def byte_size(s):
  return len(s.encode('utf-8'))

byte_size('😀') # 4
byte_size('Hello World') # 11

'''-----------------------------------------------------------------------------------------
camel
Converts a string to camelcase.

Use re.sub() to replace any - or _ with a space, using the regexp r"(_|-)+". Use title() to capitalize the first letter of each word convert the rest to lowercase. Finally, use replace() to remove spaces between words.
-----------------------------------------------------------------------------------------'''

import re

def camel(s):
  s = re.sub(r"(_|-)+", " ", s).title().replace(" ", "")
  return s[0].lower() + s[1:]

camel('some_database_field_name'); # 'someDatabaseFieldName'
camel('Some label that needs to be camelized'); # 'someLabelThatNeedsToBeCamelized'
camel('some-javascript-property'); # 'someJavascriptProperty'
camel('some-mixed_string with spaces_underscores-and-hyphens'); # 'someMixedStringWithSpacesUnderscoresAndHyphens'

'''-----------------------------------------------------------------------------------------
capitalize
Capitalizes the first letter of a string.

Capitalize the first letter of the string and then add it with rest of the string. Omit the lower_rest parameter to keep the rest of the string intact, or set it to True to convert to lowercase.
-----------------------------------------------------------------------------------------'''

def capitalize(s, lower_rest=False):
  return s[:1].upper() + (s[1:].lower() if lower_rest else s[1:])

capitalize('fooBar') # 'FooBar'
capitalize('fooBar', True) # 'Foobar'

'''-----------------------------------------------------------------------------------------
capitalize_every_word
Capitalizes the first letter of every word in a string.

Use s.title() to capitalize first letter of every word in the string.
-----------------------------------------------------------------------------------------'''

def capitalize_every_word(s):
  return s.title()

capitalize_every_word('hello world!') # 'Hello World!'

'''-----------------------------------------------------------------------------------------
decapitalize
Decapitalizes the first letter of a string.

Decapitalize the first letter of the string and then add it with rest of the string. Omit the upper_rest parameter to keep the rest of the string intact, or set it to True to convert to uppercase.
-----------------------------------------------------------------------------------------'''

def decapitalize(s, upper_rest=False):
  return s[:1].lower() + (s[1:].upper() if upper_rest else s[1:])

decapitalize('FooBar') # 'fooBar'
decapitalize('FooBar', True) # 'fOOBAR'

'''-----------------------------------------------------------------------------------------
is_anagram
Checks if a string is an anagram of another string (case-insensitive, ignores spaces, punctuation and special characters).

Use s.replace() to remove spaces from both strings. Compare the lengths of the two strings, return False if they are not equal. Use sorted() on both strings and compare the results.
-----------------------------------------------------------------------------------------'''

def is_anagram(s1, s2):
  _str1, _str2 = s1.replace(" ", ""), s2.replace(" ", "")

  if len(_str1) != len(_str2):
    return False
  else:
    return sorted(_str1.lower()) == sorted(_str2.lower())

is_anagram("anagram", "Nag a ram")  # True

'''-----------------------------------------------------------------------------------------
kebab
Converts a string to kebab case.

Break the string into words and combine them adding - as a separator, using a regexp.
-----------------------------------------------------------------------------------------'''

import re

def kebab(s):
  return re.sub(r"(\s|_|-)+","-",
    re.sub(r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+",
    lambda mo: mo.group(0).lower(), s)
  )

kebab('camelCase'); # 'camel-case'
kebab('some text'); # 'some-text'
kebab('some-mixed_string With spaces_underscores-and-hyphens'); # 'some-mixed-string-with-spaces-underscores-and-hyphens'
kebab('AllThe-small Things'); # "all-the-small-things"

'''-----------------------------------------------------------------------------------------
n_times_string
Prints out the same string a defined number of times.

Repeat the string n times, using the * operator.
-----------------------------------------------------------------------------------------'''

def n_times_string(s, n):
  return (s * n)

n_times_string('py', 4) #'pypypypy'

'''-----------------------------------------------------------------------------------------
palindrome
Returns True if the given string is a palindrome, False otherwise.

Use s.lower() and re.sub() to convert to lowercase and remove non-alphanumeric characters from the given string. Then, compare the new string with its reverse.
-----------------------------------------------------------------------------------------'''

from re import sub

def palindrome(s):
  s = sub('[\W_]', '', s.lower())
  return s == s[::-1]

palindrome('taco cat') # True

'''-----------------------------------------------------------------------------------------
reverse_string
Returns the reverse of a string.

Use string slicing to reverse the string.
-----------------------------------------------------------------------------------------'''

def reverse_string(string):
  return string[::-1]

reverse_string("snippet") #"teppins"

'''-----------------------------------------------------------------------------------------
snake
Converts a string to snake case.

Break the string into words and combine them adding _ as a separator, using a regexp.
-----------------------------------------------------------------------------------------'''

import re

def snake(s):
  return '_'.join(re.sub('([A-Z][a-z]+)', r' \1',
    re.sub('([A-Z]+)', r' \1',
    s.replace('-', ' '))).split()).lower()

snake('camelCase') # 'camel_case'
snake('some text') # 'some_text'
snake('some-mixed_string With spaces_underscores-and-hyphens') # 'some_mixed_string_with_spaces_underscores_and_hyphens'
snake('AllThe-small Things') # "all_the_smal_things"


'''-----------------------------------------------------------------------------------------
split_lines
Splits a multiline string into a list of lines.

Use s.split() and '\n' to match line breaks and create a list.
-----------------------------------------------------------------------------------------'''

def split_lines(s):
  return s.split('\n')

split_lines('This\nis a\nmultiline\nstring.\n') # 'This\nis a\nmultiline\nstring.\n'

'''-----------------------------------------------------------------------------------------
Utility
cast_list
xCasts the provided value as an array if it's not one.

Use isinstance() to check if the given value is enumerable and return it by using list() or encapsulated in a list accordingly.
-----------------------------------------------------------------------------------------'''

def cast_list(val):
  return list(val) if isinstance(val, (tuple, list, set, dict)) else [val]

cast_list('foo') # ['foo']
cast_list([1]) # [1]
cast_list(('foo', 'bar')) # ['foo', 'bar']
