# A simple number guessing game
#
import random

# Randomly chosen number to be guessed from 1 to 100
number_to_guess = random.randint(1, 100)
user_guess = 0

print("Guess the number between 1 and 100!")

# Pętla, która działa dopóki użytkownik nie zgadnie poprawnej liczby
while user_guess != number_to_guess:
    # Pobieramy liczbę od użytkownika i konwertujemy na liczbę całkowitą
    user_guess = int(input("Enter your guess: "))

    # Jeśli liczba jest mniejsza niż wylosowana
    if user_guess < number_to_guess:
        print("Too low! Try again.")
    # Jeśli liczba jest większa niż wylosowana
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    # Jeśli użytkownik trafił poprawnie
    else:
        print("Congratulations! You guessed the correct number.")
