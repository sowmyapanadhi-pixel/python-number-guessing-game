import random

numbers = random.randint(1,100)
guess=0
while guess !=numbers:
   
    guess = int(input("Guess a number between 1 and 100:"))
    if guess > numbers:
         print("Number is greater" )
    elif guess< numbers:
        print("Numbers is smaller")
    else:
        print("⭐correct!!! you got the number.")