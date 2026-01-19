import random

def number_guessing_game():
      number = random.randint(1,100)
      guess_number = None

      print("Welcome to the Number guessing game")
      print("I'm thinking of the number between 1 and 100")
      print("Can you guess the correct number? ")

      count = 0
      while guess_number != number:
            guess_number = int(input())
            count += 1
            if guess_number > number:
                  print("Too High! Try Again")
            elif guess_number < number:
                  print("Too Low! Try Again")
            else:
                  print("Congratulation! You guessed the correct number.", number)
                  print(f"You took {count} guesses.")

number_guessing_game()