# afternoon session
#exception handling
# the try block consists of code that may cause an Exception
# the except block is used to catch Exceptions that are generated from the try block
# the finally block will always run whether an exception has occured or not
  
#Example 1:(try and except)
while(True):
 try:
  # Code block where an exception might occur
    numerator = int(input("Enter the number to be divided: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print("Result:", result)
    break
 except ValueError:
    print("Invalid input. Please enter valid integers.")
 except ZeroDivisionError:
    print("Cannot divide by zero.")

#Example 2:(Raising an Exception)
try:
    raise Exception("My exception")
except Exception as e:
    print("exception has been caught")
finally:
    print("The 'try-except' block has ended.")

#Example 3:(File handling and Exception handling)
try:
 file_path = "write.txt"
 file = open(file_path, "w")

 file.write("Hello, world!\n")
 file.write("This is has been writtedn by Kato Trevor Thomas.\n")

 file.close()
 print("Data has been written to the file:", file_path)
except Exception:
   print("Error occured")

# File handling 
# Writing to a file
try:
 file_path = input("Enter the name of the file you want to write to: ")
 file = open(file_path, "w")

 message = input("Enter message you want to write: ")
 file.write(message)

 file.close()
 print("Data has been written to the file:", file_path)
except Exception:
   print("Error occured")

#reading from a file
file_name = input("Enter the name of the file: ")
file = None

try:
    file = open(file_name, 'r')
    contents = file.read()
    print("File contents:", contents)
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied to access the file.")
except IOError:
    print("Error: Input/Output error occurred.")
except Exception as e:
    print("An error occurred:", str(e))
finally:
    if file is not None:
        file.close()
        print("File closed.")

print("Execution complete.")


#reading from a line of the file
#must have a file with the name "example.txt"
try:
 with open("example.txt", "r") as file:
    line = file.readline()
    print(line)
except Exception:
   print("Error has occurred")

#reading lines from the file that appear as a list
try:
 with open("example.txt", "r") as file:
    lines = file.readlines()
    print(lines)
except:
   print("Error has occurred")

#appending data to a file
try: 
 file_path = "write.txt"
 with open(file_path, "a") as file:
    # Append data to the file
    file.write("This is additional content.\n")
    file.write("This is another line of appended content.\n")

 print("Data has been appended to the file:", file_path)
except Exception:
  print("Error occured")









