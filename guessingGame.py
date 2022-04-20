import random

num = random.randint(1, 15)
guess = None

print("NUMBER GUESSING GAME")
print("Guess a number (between 1 to 15)")
print("You get 6 chances in this game, check you luck")

chances=6

while guess != num:
    
    guess = input("Enter your guess: ")
    guess = int(guess)

    if guess == num:
        print("Congratulations!!! You won")
        break
    elif guess < num :
        print("Your guess was too low. Guess a higher number")
    else:
        print("Your guess was tooo high. guess a number higher than it")

while chances > 6:
    print("YOU LOSE!!! The number is", num)
    