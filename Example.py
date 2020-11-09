# Generates a random number. This will be the number the player has to guess.
import random

# Prints Instructions
print("Welcome To Guess The Number")
print("The aim of this game it to simply guess a randomly picked number between 1 and 40.")
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
total_points = 0
level = 0
# Once player starts game
if start.upper() == "S":
    while level < 6:
        correct_number = random.randint(1, 40)
        print(correct_number)
        for i in range(10):
            print("\nYou are on guess: ", i + 1)
            guess_number = (i + 1)
            guess = int(input("\nPlease Input Your Guess"))
            if guess == correct_number and guess_number > 4:
                print("Correct!, + 1 point")
                total_points += 1
            elif guess == correct_number and guess_number == 4:
                print("Correct! + 2 points")
                total_points += 2
            elif guess == correct_number and guess_number == 3:
                print("Correct, you have been granted 3 points.")
                total_points += 3
            elif guess == correct_number and guess_number == 2:
                print("Correct, 5 points gained!")
                total_points += 5
            elif guess == correct_number and guess_number == 1:
                print("Wow! first guess, + 10 points!")
                total_points += 10
            elif guess < correct_number and guess_number < 10:
                print("Incorrect, the number you entered is lower than the correct number. Try Again.")
            elif guess > correct_number and guess_number < 10:
                print("Incorrect, the number you entered is higher than the correct number. Try Again.")

            if guess != correct_number and guess_number == 10:
                print("\nYOU LOSE, GAME OVER\n\nYou had a total of: ", total_points, " points")
                print("\nRestarting Game...\n\nClose Game If You Do Not Want To Replay")
                level -= level
                total_points -= total_points

            if guess == correct_number:
                level += 1
                print("\nYou are on level: ", level)
                print("\nYou have a total of", total_points, "points")
                break

            if level == 6:
                print("You Have Completed Level 5. You Won The Game!")

