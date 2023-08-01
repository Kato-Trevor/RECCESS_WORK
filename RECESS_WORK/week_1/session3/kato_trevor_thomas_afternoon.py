#Exercise 1(Lists)
#1
people = ["John", "Mike", "Trevor", "Denis", "Opio"] 
print(people[1])
#2
people[0] = "Thomas"
print(people)
#3
people.append("Michelle")
print(people)
#4
people.insert(2, "Bathel")
print(people)
#5
people.pop(3)
print(people)
#6
print(people[-1])
#7
numbers = [3, 2, 1 ,4 , 5, 2, 56]
print(numbers[2:5])
#8
original_list = ['Uganda', 'Kenya', 'South Sudan']
copied_list = original_list.copy()
print(original_list)
print(copied_list)
#9
for i in original_list:
    print(i,  end=" ")
print("")
#10
animals = ['rat', 'cow', 'mouse', 'cat', 'dog']
#in ascending order
animals.sort()
print(animals)
#descending order
animals.reverse()
print(animals)
#11
for animal in animals:
    if 'a' in animal:
        print(animal)
#12
first_name = ["Kato"]
second_name = ["Trevor", "Thomas"]
full_name = first_name + second_name
print(full_name)

#Exercise 2(tuples)
x = ("samsung", "iphone", "tecno", "redmi")
#1
print(x[2])
#2
print(x[-2])
#3
my_list = list(x)
my_list[1] = "itel"
x = tuple(my_list)
print(x)
#4
my_adding_list = list(x)
my_adding_list.append("Huawei")
x = tuple(my_adding_list)
print(x)
#5
for item in x:
    print(item, end = " ")
print("")
#6
my_deleting_list = list(x)
my_deleting_list.pop(0)
x = tuple(my_deleting_list)
print(x)
#7
cities_tuple = tuple(['Kampala', 'Jinja', 'Mbarara', 'Arua'])
print(cities_tuple)
#8
a, b, c, d = cities_tuple
print(a)
print(b)
print(c)
print(d)
#9
print(cities_tuple[1:4])
#10
name1 = ("Kato")
name2 = ("Trevor", "Thomas")
names = first_name + second_name
print(names)
#11
colors = ('yellow', 'gray', 'blue')
new_tuple = colors * 3
print(new_tuple)
#12
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
num = thistuple.count(8)

print("Number of times 8 appears:", num)

#Exercise 3(sets)
#1
my_beverages = set(['beer', 'juice', 'cocktail'])
print(my_beverages)
#2
my_beverages.update(['milk', 'soda'])
print(my_beverages)
#3
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Microwave is present in the set")
else:
    print("Microwave is not present in the set")
#4
mySet.remove("kettle")
print(mySet)
#5
for item in mySet:
    print(item, end=" ")
print("")
#6
set_x = {"apple", "banana", "orange", "kiwi"}
list_x = ["grape", "pineapple"]
# Adding elements from the list to the set
set_x.update(list_x)
print(set_x)
#7
age = {34}
names = {"Kato"}
together = names.union(age)
print(together)

#Exercise 4(Strings)
#1
first = "My age is "
second = 34
print(first + str(second))
#2
txt ="      Hello,                              Uganda!   "
# Removing spaces at the beginning and end
trimmed = txt.strip()
print()
# Removing extra spaces within the string
trimmed_again = trimmed.replace(" ", "")
print(trimmed_again)
#3
print(txt.upper())
#4
print(txt.replace('U', 'V'))
#5
y = "I am proudly Ugandan"
print(y[1:4])
#6
x = "All \"Data Scientists\" are cool!"#use escape sequences
print(x)

#Exercise 5(Dictionaries)
#1
Shoes = {
"brand" : "Nick",
"color" : "black",
"size" : 40
}
print(Shoes["size"])
#2
Shoes["brand"] = "Adidas"
print(Shoes)
#3
Shoes["type"] = "sneakers"
print(Shoes)
#4
print(Shoes.keys())
#or
for key in Shoes:
    print(key, end=" ")
print("")
#5
print(Shoes.values())
#6
if "size" in Shoes:
    print("The key 'size' exists in the dictionary.")
else:
    print("The key 'size' does not exist in the dictionary.")
#7
for key, value in Shoes.items():
    print(key, value, end=", ")
print("")
#8
del Shoes["color"]
print(Shoes)
#9
Shoes.clear()
print(Shoes)
#10
user_details = {"name": "Kato", "email": "kato@gmail.com", "number": "+2567985986"}
copied_details = user_details.copy()
print(user_details)
print(copied_details)
#11
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

