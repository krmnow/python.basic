import random

number = random.randint(1,9)
guess = 0
count = 0

while guess != number and guess != "exit":
    guess = input("What's your guess?")
    if guess == "exit":

        break
