import random 



number_to_guess = random.randint(1, 100)




while True: 
    user_guess = int(input("Enter your guess: "))
    if user_guess > number_to_guess: 
        print("Too high! Try again.")
    elif user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess == number_to_guess:
        print("Congratulations! You guessed it!")
        break
