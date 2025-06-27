# Python Number Guessing Game
import random

lowest_num = 1

highest_num = 100

answer = random.randint(lowest_num, highest_num) #taking random numbers from 1 to 100

guesses = 0

print("------WELCOME-------")

is_running = True
print(("Python Number Guessing Game"))
print(f"Select the number between {lowest_num} and {highest_num}") #selecting number between 1 to 100

while is_running:
    guess = input("Guess the value: ") #input value of guesses

    if guess.isdigit(): #if user input invalid number or string
        guess = int(guess)# convert guess to integer
        guesses+=1

        if guess < lowest_num or guess > highest_num: #if user inputs negative or above range values
            print("this number is out of range!")
            print(f"Select the number between {lowest_num} and {highest_num}")

        elif guess < answer:
            print("Too low try again!")

        elif guess > answer:
            print("too high from correct answer!")

        else:
            print(f"CORRECT ! the answer was {answer}")
            print(f"the number of guesses is {guesses}")
            is_running = False
        
    else:
        print("invalid")
        print(f"please, Select the number between {lowest_num} and {highest_num} ")
        
print("Thank You!!")
    