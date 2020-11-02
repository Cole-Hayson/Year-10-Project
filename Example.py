# Generates a random number. This will be the number the player has to guess.
from random import randint
correct_number = randint(1, 50)
# Prints Instructions
print("Welcome To Guess The Number")
print("The aim of this game it to simply guess a randomly picked number between 1 and 50.")
print("After each guess you will be told if the correct number is higher or lower than your last guess")
print("You will have a total of 10 guesses and will be awarded points based on how many guesses you take.")

print("""\nThe points you will be awarded are this: 
10 points = 1 Guess
5 points = 2 Guesses
3 points = 3 Guesses
2 points = 4 Guesses 
1 point = 5 or more guesses
""")
print("For every correct guess you will be moved up one level.")
print("Your total points and current level are displayed at the end of each game and at the start of each level")
print("Good Luck and Have Fun")

# Variables
start = input('\nPlease Type "S" To Begin Game')
print(correct_number)
guess = int(input("\nPlease Input Your Guess"))
guess_number = (i + 1)
# Once player starts game
if start.upper() == "S":
    while guess != correct_number:
        for i in range(9):
            print("You are on guess: ", guess_number)
            guess = int(input("\nPlease Input Your Guess"))
            if guess < correct_number:
                print("Incorrect, the number you entered is lower than the correct number. Try Again.")
            elif guess > correct_number:
                print("Incorrect, the number you entered is higher than the correct number. Try Again.")

        final_guess = int(input("\nYou are now on your final guess. Think carefully."))
        if final_guess == correct_number:
            print("That is correct! That was a close one.\nYou have gained 1 point!")
        elif final_guess != correct_number:
            print("\nUnfortunately that is incorrect.\n\nGAME OVER")

        if guess_number == 1 and guess == correct_number:
            print("Wow, First try! You have gained 10 points")

