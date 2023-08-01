#   OOP Concepts
#class
#example1
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year 

    def start_engine(self):
        print("Engine started")

    def stop_engine(self): 
        print("Engine stopped")

my_car = Car("Toyota", "Corola", "2022")
print(my_car.make)
print(my_car.model)
print(my_car.year)
my_car.start_engine()
my_car.stop_engine()

#example2
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds")
        else:
            self.balance -= amount
    
    def display_balance(self):
        print("Account number: ", self.account_number)
        print("Balance: ", self.balance)

# create a bank account object
my_account = BankAccount("1234", 500)

#perform operations on the bank account object
my_account.deposit(500)
my_account.withdraw(200)
my_account.display_balance()

#example3
class Rectangle:
  def __init__(self, length, width):
      self.length = length
      self.width = width

  def area(self):
      return self.length * self.width
  
  def perimeter(self):
      return 2 * (self.length + self.width)
  
#creating an object
my_rectangle = Rectangle(5, 10)
print(my_rectangle.width)
print(my_rectangle.length)
#area and perimeter
print(my_rectangle.area())
print(my_rectangle.perimeter())

#example4
class Student:
    def __init__(self, name, year, course):
        self.name = name
        self.year = year
        self.course = course

    def display_details(self):
        print("Name: ", self.name)
        print("Year: ", self.year)
        print("Course: ", self.course)
    
#create a student object
my_student = Student("John Doe", 2022, "CSE")
my_student.display_details()

#example5
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
  
    def greet(self):
        print("Hello, my name is ", self.name)
        print("I am ", self.age, " years old")

#create a person object
my_person1 = Person("Jeff", 32)
my_person2 = Person("John", 22)

# accessing object attributes
print(my_person1.name)
print(my_person1.age)
print(my_person2.name)
print(my_person2.age)

# calling methods
my_person1.greet()
my_person2.greet()

#create a class Circle(exercise)
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
    def circumference(self):
        return 2 * 3.14 * self.radius

#create a circle object
my_circle = Circle(5)
print(my_circle.radius)
print(my_circle.area())
print(my_circle.circumference())

#execise
# Calculate and display employee bonus(15%) of salary (employee1: 150000, employee2: 230000)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def calculate_bonus(self):
        return self.salary * 0.15
    
    def display_details(self):
        print("Name: ", self.name)
        print("Salary: ", self.salary)
        print("Bonus: ", self.calculate_bonus())

#create object
employee1 = Employee("John Doe", 15000)
employee2 = Employee("Jane Doe", 23000)

employee1.display_details()
employee2.display_details()

#encapsulation
#example6: BankAccount
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number #encapsulates the account number attribute
        self._balance = balance #encapsulates the balance attribute

    def deposit(self, amount):
        self._balance += amount #encapsulates the deposit
    
    def withdraw(self, amount):
        if self._balance < amount:
            print("Insufficient funds")
        else:
            self._balance -= amount #encapsulates the withdraw

    def get_balance(self):
        print("Account number: ", self._account_number)
        print("Balance: ", self._balance) 

#create a bank object
my_account = BankAccount("123432", 1000)

#access the bank object and modify the encapsulated attributes indirectly
print(my_account._account_number)
print(my_account._balance)
my_account.deposit(500)
print(my_account._balance)
my_account.withdraw(100)
print(my_account._balance)

#execise 2: Convert temperature 37 degrees celsius to Fahrenheit

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    def convert_to_fahrenheit(self):
        return (self._celsius * 9 / 5) + 32
    
temp = Temperature(37)
print(temp.convert_to_fahrenheit())
print(temp._celsius)

#learn encapsulation in python
#Assignment1: show encapsulation with employee information to
#give a pay incrementation

class Employee:
    def __init__(self, employeeID, name, salary):
        self._employeeID = employeeID
        self._name = name
        self._salary = salary
    
    def increment_salary(self, amount):
        self._salary += amount
        
    def display_details(self):
        print("EmployeeID: ", self._employeeID)
        print("Name: ", self._name)
        print("Salary: ", self._salary)

employee_one = Employee("m1", "Mike", 85000)
employee_one.display_details()

employee_one.increment_salary(15000)
employee_one.display_details()