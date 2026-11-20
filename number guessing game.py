import random

secret = random.randint(1, 50)
attempts = 5

print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 50")

while attempts > 0:
    guess = int(input("Enter your guess: "))
    
    if guess == secret:
        print("Congratulations! You won!")
        break
        
    elif guess < secret:
        print("Too low!")
        
    else:
        print("Too high!")
        
    difference = abs(secret - guess)
    
    if difference <= 5:
        print("Hint: Very close!")
    elif difference <= 10:
        print("Hint: Close!")
    else:
        print("Hint: Far away!")
        
    attempts = attempts - 1
    
    print("Remaining lives:", "❤️ " * attempts)
    
if attempts == 0 and guess != secret:
    print("Game Over!")
    print("The secret number was:", secret)
