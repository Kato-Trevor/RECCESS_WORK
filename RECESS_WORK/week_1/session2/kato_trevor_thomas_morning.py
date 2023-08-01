# #control flow-session2
#if, elif and else
student_number = 32
num = 3
if (student_number<18):
    print("you are understudent_number")
elif(student_number >= 18 or student_number <=65):
   print("you are an adult")
else:
    print("you are a senior")

if (num%2 == 0):
    print("x is an even number")
elif(num%2 != 0):
    print("x is an odd number")
else:
    print("x is not a number")

my_sequence = [2, 3, 1, 4, 5, 6]
for i in my_sequence:#for loops
    print(i)

fruits =  ["Banana", "Strawberry", "Lemon", "Watermelon"]
for fruit in fruits:
    print(fruit, end=' ')

fruit_count = 0
while fruit_count < len(fruits):#while loops
    print(fruits[fruit_count], end=" ")
    fruit_count += 1
print("")
number = 0
while number<10:
    print(number, end=" ")
    number += 1
i = 0
print("")
#continue statements
while (i<10): #printing even numbers with continue
    if(i%2 != 0):
        i += 1
        continue
    else:
        print(i, end=" ")
        i += 1
#break statements
print("")
j = 1
while(j<10):#printing first five digits with break
    if(j == 5):
        break
    else:
        print(j, end=" ")
        j += 1
print("")
#exception handling(try, except, finally)
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
 
try:
    raise Exception("My exception")
except Exception as e:
    print("exception has been caught")
finally:
    print("The 'try-except' block has ended.")

#responding to user's input
feeling_responses = {
    'neutral': "I guess there was nothing exciting today",
    'happy': "Yeyyy, I'm glad you're happy",
    'sad': "I'm sorry you feel that way",
    'excited': "Woww, enjoy the excitment!",
    'tired': "I'm guessing you had a long day"
}

user_feeling = input("How are you feeling? ")

user_feeling = user_feeling.lower()

if user_feeling in feeling_responses:
    system_response = feeling_responses[user_feeling]
    print(system_response)
else:
    print("I'm sorry, I don't have a response for that feeling.")

#health responses basing on scale of 1 to 10

feeling_responses = {
    1: "I'm sorry to hear that you're feeling very low.",
    2: "I understand that you're feeling down.",
    3: "I hope your day gets better soon.",
    4: "I'm here to listen if you need to talk.",
    5: "I'm glad to hear you're feeling okay.",
    6: "That's good to know!",
    7: "I'm happy that you're doing well.",
    8: "That's great! Keep up the positive energy.",
    9: "You seem to be having an amazing day!",
    10: "Wow! You're on top of the world!"
}
while(True):
 try:
  user_feeling = int(input("On a scale of 1 to 10, how are you feeling? "))
  if 1 <= user_feeling <= 10:
    system_response = feeling_responses[user_feeling]
    print(system_response)
    break
  else:
    print("Please enter a number between 1 and 10.")
 except ValueError:
    print("Invalid input. Please enter valid integers from 1 to 10.")
    