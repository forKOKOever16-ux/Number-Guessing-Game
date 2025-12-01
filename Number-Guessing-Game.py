import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)
guesses = 0
is_running = True

print("Python Number Guessing Game 🔢")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:

    guess = input("Enter your guess: ")

    if guess.isdigit(): # تتأكد إن المدخل أرقام فقط بدون حروف. , isdigit()
        guess = int(guess) # هنا يتحول من "25" (string) إلى 25 (integer)
        guesses += 1  # يزيد عدد المحاولات

        if guess < lowest_num or  guess> highest_num:
            print("That number is out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}")

        elif guess < answer:
            print("Too low! Try again!🔄")
        elif guess > answer:
            print("Too high! Try again!🔄")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False

    else:
        print("Invalid guess: ")
        print(f"Please select a number between {lowest_num} and {highest_num}")