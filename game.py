'''
Develop a guessing game where the computer will randomly choose any one of the 10 digits and the user gets 3 chances to guess the correct number.
'''
import random

# Enter choice list below
computer_number = random.choice()
print("The computer has choosen its number. Now it is your turn to guess...")

user_lives = 3
while user_lives > 0:
    print("You have {} lives remaining.".format(user_lives))
    guess = int(input("Enter your guess: "))
    
    if guess == computer_number:
        print("CONGRATULATIONS!! YOU HAVE GUESSED THE NUMBER CORRECTLY.")
        break
    else:
        user_lives = user_lives - 1
        print("Sorry wrong guess. Try again.")
        if guess > computer_number:
            print("HINT: The number is smaller than the number you entered")
        else:
            print("HINT: The number is larger than the number you entered")
        
if user_lives == 0:
    print("GAME OVER!")
    print("The computer's number was {}".format(computer_number))