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
