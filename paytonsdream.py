import random


value = random.randint(1, 10)
print("Please enter a digit from 1-10 in which you think I saw in my dream: ")
int3 = input()
if value == int3:
    print("Congrats. That was exactly what I dreamt!")
else:
    print("Sorry, that wasn't quite what I visioned in my dream...")
print("Your answer was: " + int3 + " The real answer was: ")
print(value)
