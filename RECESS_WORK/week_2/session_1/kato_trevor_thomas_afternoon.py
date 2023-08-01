#afternoon session
#functions
#group blocks of code, that bring reusable, clean and maintainable code

def function_name():
    print("This is a function")
    print("This is also part of the function")

#calling a function
function_name()

#arguments and parameters
def afternoon(first_name, last_name):
              print(f"My name is {first_name} {last_name}")

afternoon("Kato", "Trevor")

#modules
def product(a,b):
  return a * b
def add(a,b):
  return (a+b)

# import session_3# here we are importing the module withtin itself
# print(session_3.product(2,3))

#input and output in python
#example of input

#example1
name = input("Enter your name: ")
print(f"My name is {name}")

# #example2
number = int(input("Enter a number: "))
product = number * number
print("The square is ", product)

#example3-multiple inputs in python
s,r,w = map(int, input("Enter the values: ").split()) #the map function is used to convert the input to a specific data type 
print("The values are: ", end=" ")
print(s,r,w)  

#how to capture input from a tuple
w = (2,4,6,5,8)
print("Current tuple")
print(w)
print(type(w))

e = list(w)
e.append(int(input("Enter a new value: ")))
w = tuple(e)
print("updates tuple: ")
print(w)

#how to deal with input from a set
s = {4, 3, 2}
print(s)
s.add(int(input("enter a value to be added: ")))
print(s)

#lists
my_list = list(map(int, input("Enter a list of values: ").split()))
my_set = set(map(int, input("Enter a set of values: ").split()))

print(my_list)
print(my_set)
