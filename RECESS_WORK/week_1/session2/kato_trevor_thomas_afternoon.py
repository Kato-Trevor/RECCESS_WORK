#afternoon session
# dicts(ordered, mutable but cannot have duplicates)
my_dict = {"phone":"iphone", "iphone_model":"iphone15", "year":"2023"}
print(my_dict)
#length
print(len(my_dict))
#data type
print(type(my_dict))
#accessing items
print(my_dict["phone"])

y = my_dict.get("iphone_model")
print(y)

#keys
print(my_dict.keys())
#values
print(my_dict.values())

#checking if a key exists
if "year" in my_dict:
    print("Key 'year' exists in the dictionary.")
else:
    print("Key 'year' does not exist in the dictionary.")

#modifying items
my_dict["iphone_model"] = "iphone13"
print(my_dict)

#adding and removing items from the dictionary
my_dict["origin"] ="New York"

#using the pop method
my_dict.pop("iphone_model")
print(my_dict)

#using the del statment
del my_dict["origin"]
print(my_dict)

for i in my_dict:#printing keys
    print(i, end=" ")
print(" ")
for j in my_dict.values():#printing values
    print(j, end=" ")
print(" ")
for key, value in my_dict.items():
    print(key, value, end=", ")

#nested dictionaries
students = {
    'Tracy': {'student_number': 25, 'course': 'BIST'},
    'Tyra': {'student_number': 23, 'course': 'BSSE'},
    'Kato': {'student_number': 28, 'course': 'CS'}
}

# Accessing nested dictionaries
for name, details in students.items():
    print(name)
    print('student_number:', details['student_number'])
    print('course:', details['course'])
    print()

#adding items
students['Mike'] = {'student_number': 30, 'course': 'BSSE'}
print(students)

#removing using pop method
removed_student = students.pop('Kato')
print(removed_student)
#removing using del keyword
del students['Mike']
print(students)

#numbers
w = 10#int
r = 3.9#float
s = 2j#complex

print(type(w))
print(type(r))
print(type(s))

#integers
a = 34
b = 455444
c = -34322

print(type(a))
print(type(b))
print(type(c))

#floats
d = 3.4
e = 45.76
f = -5643.766

print(type(d))
print(type(e))
print(type(f))

z = complex(w)
print(z)
print(type(z))

#casting
h = int(45)
y = int(309876)
u = int("7")#becomes a 7
print(h)
print(y)
print(u)

# strings
# assigning a string to ta variable
t = "Afternoon"
#multiline strings
v = """Hello
this is my multi line string
check it out"""
print(v)
#accessing string items
print(t[0])

#length of string
print("length of the string is: ", len(t))

#for loops in strings
my_string = "Hello world"
for char in my_string:
    print(char, end=", ")
print()

#slicing in strings
sub_string1= my_string[3:5]
print(sub_string1)
sub_string2 = my_string[6:11]
print(sub_string2)

#modifying strings
str = "Hello"
print(str.lower())
print(str.upper())

#remove the white space
str2 =  "     After noon"
print(str2)
print(str2.strip())

str_first = "Hello"
str_second = "world"
together = str_first +" "+ str_second
print(together)

#combining strings with numbers
age = 54
# str_num = "My age is"+ age #error appears
str_num = "My age is {}"
# print(str_num.format(age))

quantity = 3
item_number = 567
price = 46.96
my_order = "I want {0} pieces of item {1} for {2} dollars"
print(my_order.format(quantity, item_number, price))

# boolean
print(20<10)
print(30 == 40)
print(30>10)

print(bool(-34))

name = "Kato"
integ = 30

print(bool(name))
print(bool(integ))

#use a condition to show how to use booleans
digit = 0
while(digit<20):#getting multiples of 3
   if(digit%2 == 0):
      print(digit, end=" ") 
   digit += 1
