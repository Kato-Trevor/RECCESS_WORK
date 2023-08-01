#Context managers practice
class ContextManager:
   def __init__(self):
      print("this is constructor")

   def __enter__(self):#returns the resource that needs to be managed 
      print("this is the enter method")

   def __exit__(self, exc_type, exc_value, exc_traceback):#performs the cleanup operations.
      print("this is the exit method")

with ContextManager() as context:
   print("This is the with block")

#Assignment
#use of Context Managers with File Handling
class FileHandler:
   def __init__(self, filename, mode):
      self.filename = filename
      self.mode = mode
      self.file = None

   def __enter__(self):
     self.file = open(self.filename, self.mode)
     return self.file
   
   def __exit__(self, exc_type, exc_value, exc_traceback):
      self.file.close()

with FileHandler('test.txt', 'w') as f:
   f.write("Hello World")

#check if file is closed
print(f.closed)

#use of Context Managers with Database connections
import sqlite3

class DatabaseConnection:
    def __init__(self, database_name):
        self.database_name = database_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.database_name)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()

# Example usage
database_name = "example.db"

with DatabaseConnection(database_name) as conn:
    # Perform database operations using the connection
    print("This is the with block")


#Show a multithreading and multiprocessing  that allows
#  us to run the function for different amounts of time.
import threading
import time

def run_function(seconds):
    print(f"Function running for {seconds} seconds...")
    time.sleep(seconds)
    print("Function completed!")

thread1 = threading.Thread(target=run_function, args=(2,))
thread2 = threading.Thread(target=run_function, args=(4,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

import multiprocessing
import time

def run_function(seconds):
    print(f"Function running for {seconds} seconds...")
    time.sleep(seconds)
    print("Function completed!")
if __name__ == "__main__":
 # Create processes to run the function for different amounts of time
 process1 = multiprocessing.Process(target=run_function, args=(2,))
 process2 = multiprocessing.Process(target=run_function, args=(4,))

 # Start the processes
 process1.start()
 process2.start()

 # Wait for the processes to finish
 process1.join()
 process2.join()








