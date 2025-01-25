def number_guessing_game():
    number = int(input("Enter the random number (between 1 and 100): ")) 
   
    while True:
        guess = int(input("Guess the number between 1 and 100: "))  
        

        if guess < number:
            print("Too Low!")
        elif guess > number:
            print("Too High!")
        else:
            print(f"Congratulations! You guessed the number {number}.")
            break

number_guessing_game()
