# Generates a random number. This will be the number the player has to guess.
from random import randint
correct_number = randint(1, 100)

# Prints Instructions
print("Welcome To Guess The Number")
print("The aim of this game it to simply guess a randomly picked number between 1 and 100.")
print("You will have a total of 10 guesses and will be awarded points based on how many guesses you take.")
print(""" The points you will get are this: 
10 points = 1 Guess
5 points = 2 Guesses
3 points = 3 Guesses
2 points = 4 Guesses 
1 point = 5 or more guesses
""")
