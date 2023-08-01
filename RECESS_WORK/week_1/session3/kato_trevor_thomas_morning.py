#morning session
"""
-Comparison operators
== equal to
!= not equal !==
> greater than
< less than
>= greater than or equal to
<= less than or equal to

-Assignment operators
Assign value: '='
Add value: '+'
Add and assign a value: '+='
Subtract and assign a value: '-='

-membership operator
In: 'in' operator: checks if a value exists in a sequence
Not in: 'not in' operator: checks if a value does not exist in a sequence

-Identity operators
Is: 'is' operator: checks if two values are the same
Is not: 'is not' operator: checks if two values are not the same
"""

#addition
x = 50 + 45
print(x)

#subtraction
y = 50 - 45
print(y)

#multiplication
z = 50 * 45
print(z)

#division
a = 50 / 45#floating point division
print("floating-point division: ",a)

#divide
b = 50 // 45#floor division
print("floor division: ",b)

#modulus
c = 50 % 45
print(c)

#exponention
d = 2 ** 4
print(d)

#comparison operators
a = 15
b = 9

#greater than
if a > b:
    print("a is greater than b")
    print(a>b)

#less than
if a < b:
    print("a is less than b")
    print(a<b)

#greater than or equal to
if a >= b:
    print("a is greater than or equal to b")
    print(a>=b)

#less than or equal to
if a <= b:
    print("a is less than or equal to b")
    print(a<=b)

#equal to
if a == b:
    print("a is equal to b")
    print(a==b)

#not equal to
if a != b:
    print("a is not equal to b")
    print(a!=b)

#examples with logical operators
#logical operators
a = True
b = False

#logical AND
print(a and b)

#logical OR
print(a or b)

#logical NOT
print(not a)
print(not b)

#assignment operators
#compound assignment operators
a = 5
b = 3
print(a)
print(b)
#add and assign
a += 5
print(a)
#subtract and assign
b -= 5
print(b)
#multiply and assign
b *= 5
print(b)
#divide and assign
d = 19
d /= 5
print(d)

#modulus and assign
e = 19
e %= 5
print(e)
#exponentiation and assign
f = 2
f **= 4
print(f)

#membership assignment operators
cars = ["Jeep", "BMW", "RollRoyce", "Tesla"]
if "Jeep" in cars:
   print("Jeep is in the list")
   print("Tesla" in cars)
   print("Toyota" in cars)

#identity operators
x = 10
y = 10

#is operator
print(x is y)
print(x is not y)

z = [1, 2, 3, 4]
w = [1, 2, 3, 4]

print(z is w)
print(w is not z)

#bitwise operators
"""
bitwise operators are used to perform operations on individual bits
of binary numbers

Bitwise AND (&): performs a bitwise AND operaion between the corresponding
bits of two integers.
Bitwise OR ('|'): performs a bitwise OR operation between the corresponding
bits of two integers.
Bitwise XOR(^): performs bitwise XOR operation
Bitwise NOT (~): performs bitwise NOT operation
Bitwise left shift (<<): performs bitwise left shift operation  
Bitwise right shift (>>): performs bitwise right shift operation
"""
#example
a = 10
b = 20
# #bitwise AND operations
result_and = a & b
print(result_and)

# #bitwise OR operations
result_or = a | b
print(result_or)

# #bitwise XOR operations
result_xor = a ^ b
print(result_xor)

# #bitwise NOT operations
result_not = ~a
print(result_not)

#bitwise left shift
result_left_shift = a << 2
print(result_left_shift)

#bitwise right shift
result_right_shift = a >> 2
print(result_right_shift)

#calculator
#make functions add, subtract, multiply and divide
def add(x, y):
    print(x + y)
def subtract(x, y):
    print(x - y)
def multiply(x, y):
    print(x * y)
def divide(x, y):
    print(x / y)

#call functions
def main():
  print("Welcome to calculator")
  while(True):
   try:
    first = float(input("First number: "))
    second = float(input("Second number: "))
    operator = input("Operator: ")
    if operator == "+":
        add(first, second) 
    elif operator == "-":
        subtract(first, second)
    elif operator == "*":
        multiply(first, second)
    elif operator == "/":
        divide(first, second)
    break
   except Exception:
       print("Invalid input")
       
main()

#using tkinter learn,
#assignment-create a simple calculator program with a GUI interface.
#make the title of the calculator program window with your name

import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operations.get()

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            result = num1 / num2

        label_result.config(text="Result: " + str(result))
    except ValueError:
        label_result.config(text="Invalid input!")

# main window
window = tk.Tk()
window.title("Kato Trevor Thomas")

# number input fields
label_num1 = tk.Label(window, text="Number 1:")
label_num1.pack()
entry_num1 = tk.Entry(window)
entry_num1.pack()

label_num2 = tk.Label(window, text="Number 2:")
label_num2.pack()
entry_num2 = tk.Entry(window)
entry_num2.pack()

# operation selection dropdown
operations = tk.StringVar()
operations.set("Pick operation")
dropdown = tk.OptionMenu(window, operations, "Add", "Subtract", "Multiply", "Divide")
dropdown.pack()

#calculate button
button_calc = tk.Button(window, text="Calculate", command=calculate)
button_calc.pack()

# the result
label_result = tk.Label(window, text="Result: ")
label_result.pack()

# Start the main event loop
window.mainloop()


