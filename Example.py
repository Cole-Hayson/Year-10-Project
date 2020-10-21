# Generates a random number. This will be the number the player has to guess.
from random import randint
correct_number = randint(1, 100)
print(correct_number)
# Prints Instructions
print("Welcome To Guess The Number")
print("The aim of this game it to simply guess a randomly picked number between 1 and 100.")
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
guess1 = input("Please Input Your First Guess")

# Once player starts game
if start == "S":
    guess1 = input("Please Input Your First Guess")
    if guess1 == correct_number:
        print("Wow, that's amazing you got it right first time! \nYou have gained 10 Points!")
