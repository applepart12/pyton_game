import random
def number_guessing_game():
  print("Welcome to the Number Guessing Game! ")
  print("I'm thinking of a number between 1 to 100, ")

# Generation of a random number between 1 and 100
secret_number = random.randint(1,100)
attempts = 0


while True:
    try:
        #Get the player's guess
        guess = int(input("Make a guess"))
        attempts += 1
        
        
        #Check if the guess is too high , too low or correct
        if guess < secret_number:
            print("Too low")
        elif guess > secret_number:
            print("Too high")
        else:
            print(f"Congratulations! You guessed the number {secret-number}in{attempts}attempts.")
            break#Exit the loop when the correct guess is made
    except ValueErrors:
        print("Please enter a valid number.")

if _name =="_main_":
  number_guessing_game()
        