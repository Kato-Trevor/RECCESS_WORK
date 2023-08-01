#Morning session
#Advanced Topics in Python

"""_summary_
-Regular Expression
-Generators and Iterators
-Decorators
-Context Managers-get from his youtube
-Multithreading and multiprocessing-get from his youtube
"""

#Regular Expression
"""
\d: Matches any digit (0-9)
\w: Matches any alphanumeric character (a-z, A-Z, 0-9 and Underscore)
\s: Matches any whitespace character (space, tab, newline, etc.)
.: Matches any character except a new line
*: Matches zero or more occurrences of the preceding character or group
+: Matches one or more occurrences of the preceding character or group
?: Matches zero or one occurrence of the preceding character or group
[ ]: Matches any character within the square brackets
[^ ]: Matches any character not within the square brackets
^: Matches the start of a line
$: Matches the end of the line
"""

#Matching and searching
#regex re.match, re.search(), re.findall()

#example1-Demonstartig regex | Match first word, Match group word, match all numbers
import re
text = "Hello my name is Kato Trevor, I am a programmer with 15 years of experience"

#match first word
match = re.search(r"\b\w+\b", text)

if match:
    print("Match: ", match.group())

matches = re.findall(r"\d+", text)
print("matches: ", matches)

def validate_email(email):
  pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
  if re.match(pattern, email):
     return True
  else:
     return False

#example usage
email1 = "kato99@gmail.com"
email2 = "kato99@gmailcom"
print(validate_email(email1))
print(validate_email(email2))

#password validation

def validate_password(password):
    # Regular expression pattern for password validation
    pattern = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"

    if re.match(pattern, password):
        return True
    else:
        return False

# Test the function with example passwords
passwords = ["Abc123", "password123", "abcdefg", "12345678"]

for password in passwords:
    if validate_password(password):
        print(f"{password} is a valid password.")
    else:
        print(f"{password} is an invalid password.")


#generators and iterators
# 'yield' generator
# iterator '__iter__' "__next__" iterator

def factorial(n):
   #return the factorial of a number
   if n == 0:
      return 1
   else: 
      return n * factorial(n - 1)

#print the factorial of a number from 1 to 10
for i in range(1, 10):
   print(factorial(i))

#example 3
def factorial(n):
   if n == 0:
      yield 1
   else:
    #   yield n * factorial(n - 1)
      fact = 1
      for i in range(1, n+1):
        fact *= i
      yield fact

for i in range(1, 6):
   print(*factorial(i))

#example 3
#generate a function that yields te square of numbers from 1 to 10
def squares():
   for i in range(1, 10):
      yield i ** 2

#create an iterator object that yields the square of numbers from 1 to 10

squares_iterator = squares()

#print the first five squares fro 1 to 10
for i in range(5):
   print(next(squares_iterator))


#decorators-allow you to modify the behavior of functions or classes without
# directly changing the source code

def my_decorator(func):
   def inner():
      print("This is my decorator")
      func()
   return inner
   
@my_decorator
def outer_decorator():
   print("This is the outer decorator")

outer_decorator()

#Context managers in python- These are used to facilitate the proper 
# handling of resources for example in file handling
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

# Usage:
with FileManager("example.txt", "w") as file:
    file.write("Hello, World!")


#Mutlithreading in python- tis is the ability of a processor to execute multiple threads concurrently. 
import threading

def print_numbers():
    for i in range(1, 6):
        print(i)

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(letter)

# Create two threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()

print("Finished")


