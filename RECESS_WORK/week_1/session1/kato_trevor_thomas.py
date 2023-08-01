#morning session-session1
#simple python code
print("Hello world")

#this is a single line comment

"""Multi line 
comment right here
comment"""

#variables
name = "Hello"
first_number = 4
second_number = 3

print(first_number+second_number)
print(name) 

#data types

#numerical
my_float = 3.4 #float 
my_int = 12345 #int
my_string = "hello world" #string

#logical values
my_bool = True #bool
my_other_bool = False #bool

#sequence types
#set types, dicts, ranges, item dict, none types
my_tuple = (my_float, my_int, my_string) #tuple
my_list = [my_float, my_int, my_string] #list
my_dict = {'name':name, 'first_number':first_number, 'second_number':second_number} #dict

print(my_float)
print(my_int)
print(my_string)
print(my_dict)
print(type(my_dict))
print(my_list)
print(type(my_list))
print(my_tuple)
print(type(my_tuple))

my_set = {3, 2, 1, 5, 2, 8}
print(my_set)
print(type(my_set))

#ranges
for i in range(5):
    print(i)

#none types
my_none_variable = None
print(my_none_variable)

#=================================

#afternoon session
#more on data types
my_other =7j
my_string = "Hello"
print(type(my_string))
print(type(my_other))

#lists(ordered, mutable and allow duplicate values)
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 5, 4, 3]
my_names = ["Trevor", "Peter", "Blessing", "Peter", "Blessing", "John"]
print(my_list)

#length of list
print(len(my_list))

#list type
print(type(my_list))

#accessing elements
print(my_list[4])
#with negative indices
print(my_names[-2])
print(my_names[-1])

#accessing a range of items
print(my_list[3:11])
print(my_list[:5])
"""first digit is the index of the first element
 in the range and second index is item after the range is obtained"""

#adding to the list with append
my_list.append(111)
print(my_list)
#adding items with insert
my_names.insert(0, "Kato")
print(my_names)

#removing from the list with remove
my_names.remove("Kato")
print(my_names)
#removing items with pop
my_names.pop(4)
print(my_names)

#tuples(ordered, immutable collection)
phones = ("samsung", "iphone", "Techno")
print(phones)

#allow for duplicate values       
phones = ("samsung", "iphone", "Techno", "Techno", "samsung")
print(phones)

#exercise use the len with this tuple
print(len(phones))

#showing datatypes
print(type(phones))

#exercise- accessing elements of tuples
#using square brackets
print(phones[2])#indices
print(phones[-1])#negative indices
print(phones[1:4])#slicing

#adding to tuples(first convert tuple to a list)
my_tuple_list = list(phones)
my_tuple_list.append("nokia")
print(my_tuple_list)
phones = tuple(my_tuple_list)
print(phones)

#adding tuples together
tuple1 = ("red", "green", "yellow", "blue")
tuple2 = ("car", "bike", "motorcycle", "bus")
together = tuple1 + tuple2
print(together)
tuple1 += tuple2
print(tuple1)

#iterating through tuples
for y in tuple2:
    print(y)

#sets(also similar to tuples but can have values added and deducted, sets are also unordered)
my_set = {5, 3, 2, 15, 6, 34, 23}
print(my_set)
#duplicates in sets
my_set = {5, 3, 2, 15, 6, 34, 23, 5, 5, 5}
print(my_set)#will not print duplicates

#exercise - find the lengths of sets, data type, accessing elements, adding items and adding two sets together
print(len(my_set))
print(type(my_set))

#accessing elements in sets
for x in my_set:
    print(x, end=' ')#to have the elements on one line

#adding set elements
my_set.add(999)
print(my_set)

my_set.update(together)
print(my_set)

#removing elements
my_set.remove("blue")
print(my_set)

my_set.discard("green")
print(my_set)

#adding two sets together
set1 = {1, 2, 3}
set2 = {"one", "two", "three"}
combined = set1.union(set2)
print(combined)

combined2 = set1 | set2 
print(combined2)







