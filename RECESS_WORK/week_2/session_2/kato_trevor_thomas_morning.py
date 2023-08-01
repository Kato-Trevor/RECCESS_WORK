# #inheritance in python
class Person:
    def __init__(self, name):
      self.name = name
    
    def isEmployee(self):
       return False

class Employee(Person):
   def isEmployee(self):
       return True

#creating objects
p1 = Person("John")
p2 = Employee("Mary")

print(p1.name, p1.isEmployee())
print(p2.name, p2.isEmployee())

#the self keyword->myObject.method(arg1, arg2) is the same as myClass.method(myObject, arg1, arg2)
class myClass:
   attr1 = "dog"
   def __init__(self):
      print("myClass object has been created")
  
   def myMethod(self):
      print("myMethod object has been called")

class myClass2:
   attr2 = "three"
   def __init__(somename):
      print("myClass2 object has been created")
    
   def myMethod(somename, arg1):
      print(f"This is the {arg1}")

myObj = myClass2()
myObj.myMethod("dog")

myObj2 = myClass()
myObj2.myMethod()

#init functions when dealing with inheritance
class Parent:
   def __init__(self, name):
      self.name = name
    
class Child(Parent):
   def __init__(self, name, age, course):
       self.course = course
       self.age = age
       self.name = name
   

myOther = Child("Kato", 34, "BIST")
print(myOther.course)
print(myOther.name)

#morning session
#inheritance
#Example 1
class Animal:
   def __init__(self, name):
      self.name = name


   def eat(self):
      print(f"{self.name} is eating...")


class Dog(Animal):
   def bark(self):
      print(f"{self.name} is barking...")
  

class Cat(Animal):
   def meow(self):
      print(f"{self.name} is meowing...")


# creating animal objects
animal = Animal("Generic animal")
myDog = Dog("Fido")
myCat = Cat("Fluffy")

# invoke call eat method
animal.eat()
myDog.eat()
myDog.bark()
myCat.eat()
myCat.meow()

# Example 2
class Vehicle:
   def __init__(self, brand, color):
      self.brand = brand
      self.color = color


   def display_info(self):
      print("Brand: ", self.brand)
      print("Color: ", self.color)
  

   def move(self):
      print("Moving the vehicle...") 

class Car(Vehicle):
   def __init__(self, brand, color, num_wheels):
       super().__init__(brand, color)
       self.num_wheels = num_wheels

  
   def display_info(self):
      super().display_info()
      print("Number of wheels, ", self.num_wheels)

   
   def honk(self):
      print("Honking the horn...")

#create a Car object
my_car = Car("Toyota","Red", 4)

#access and modify car attributes
print("Brand: ", my_car.brand)
my_car.color = "Gray"

#invoke car methods
my_car.display_info()
my_car.move()
my_car.honk()

#Exercise
#demonstrate using inheritance calculation of area and perimeter of a circle and rectangle respectively
class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

   
import math

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
    

#creating objects of the Circle and the Rectangle
my_circle = Circle(5)
my_rectangle = Rectangle(10, 20)

#get area and perimeter
print("Area of circle: ", my_circle.calculate_area())
print("Area of rectangle: ", my_rectangle.calculate_area())

print("Perimeter of circle: ", my_circle.calculate_perimeter())
print("Perimeter of rectangle: ", my_rectangle.calculate_perimeter())

#multiple inheritence
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating...")

    def display_info(self):
        print(f"Name: {self.name}")

class Flyable:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} is flyable...")

class Bird(Animal, Flyable):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

    def display_info(self):
        super().display_info()
        print(f"Species: {self.species}")
        print(f"name: {self.name}")

# create a bird object
my_bird = Bird("Donald", "bird")

# invoke the bird methods
my_bird.eat()
my_bird.fly()
my_bird.display_info()

#method overridding
class Animal:
    def make_sound(self):
        print("Animal is making a sound")

class Dog(Animal):
    def make_sound(self):
        print("Dog is barking")
    
class Cat(Animal):
    def make_sound(self):
        print("cat is meowing")


def make_animal_sound(animal):
    animal.make_sound()

#creating objects
dog = Dog()
cat = Cat() 
animal = Animal()

#calling make_animal_sound function
make_animal_sound(dog)
make_animal_sound(cat)
make_animal_sound(animal)

#polymorphism allows you to mwrite code that can work with different objects

#method overridding
#method overloading allows a class to have multiple methods with the same name but different parameters

class Shape:
    def calculate_area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius**2
    
    def calculate_circumference(self):
        return 2 * 3.14 * self.radius
    
# create shape objects
rectangle = Rectangle(5,5)
circle = Circle(5)

# calculate and display area
print("Rectangle area: ",   rectangle.calculate_area())
print("Circle area: ", rectangle.calculate_area())

# abstraction
#allows you to focus on essential features and hide from unnecessary details

#example 5: Demonstrate abstractions  
from abc import *

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass   
    
    @abstractmethod
    def stop(self):
        pass
    
class Car(Vehicle):
    def start(self):
        print("Starting the car...")
    
    def stop(self):
        print("Stopping the car...")

    
class Truck(Vehicle):
    def start(self):
        print("Starting the truck...")
    
    def stop(self):
        print("Stopping the truck...")

#create vehicle objects
car = Car()
truck = Truck()

#start and stop vehicles
truck.start()
car.start()

truck.stop()
car.stop()

# exercise 2
# Demonstrate abstraction by calculating the area of a circle and rectangle 
from abc import *

class Shape(ABC):
    @abstractmethod
    def calc_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        print("Area of circle is ", 3.14159 * self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_area(self):
        print("Area of rectangle is ", self.width * self.length)

#create the objects
my_circle = Circle(5)
my_rectangle = Rectangle(10, 20)

#getting the areas
my_circle.calc_area()
my_rectangle.calc_area()

#assignment
# create a receipt printing prograam with GUI interface
# a more advanced detail earns you more points
# deadline 01-July 2023 Time 5:00pm EAT

import tkinter as tk

class MyReceipt(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kato Trevor Thomas")
        self.geometry("400x300")

        self.create_widgets()
        self.receipt_items = []

    def create_widgets(self):
        self.item_label = tk.Label(self, text="Item Name:")
        self.item_label.pack()
        self.item_entry = tk.Entry(self)
        self.item_entry.pack()

        self.price_label = tk.Label(self, text="Item Price:")
        self.price_label.pack()
        self.price_entry = tk.Entry(self)
        self.price_entry.pack()

        self.quantity_label = tk.Label(self, text="Item Quantity:")
        self.quantity_label.pack()
        self.quantity_entry = tk.Entry(self)
        self.quantity_entry.pack()

        self.add_button = tk.Button(self, text="Add Item", command=self.add_item)
        self.add_button.pack()

        self.separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN)
        self.separator.pack(fill=tk.X, padx=5, pady=5)

        self.receipt_text = tk.Text(self, height=10)
        self.receipt_text.pack()

        self.total_label = tk.Label(self, text="Total Amount:")
        self.total_label.pack()
        self.total_value = tk.Label(self, text="")
        self.total_value.pack()

        self.print_button = tk.Button(self, text="Print Receipt", command=self.print_receipt)
        self.print_button.pack()

    def add_item(self):
        item = self.item_entry.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()

        item_info = f"{item} - Quantity: {quantity}, Price: UGX {price}"
        self.receipt_items.append((item, int(quantity), float(price)))

        self.receipt_text.insert(tk.END, item_info + "\n")

        self.item_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

        self.calculate_total()

    def calculate_total(self):
        total = sum(quantity * price for _, quantity, price in self.receipt_items)
        self.total_value.config(text=f"UGX {total:.2f}")

    def print_receipt(self):
     receipt_items = "\n".join(f"{item} - Quantity: {quantity}, Price: UGX {price}" for item, quantity, price in self.receipt_items)
     total = sum(quantity * price for _, quantity, price in self.receipt_items)
     receipt = f"{receipt_items}\nTotal Amount: UGX {total:.2f}"
     print(receipt)
 

if __name__ == "__main__":
    app = MyReceipt()
    app.mainloop()