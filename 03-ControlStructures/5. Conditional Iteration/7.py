import time

# Pobranie liczby od użytkownika
countdown = int(input("Enter the countdown starting number: "))

# Odliczanie
while countdown > 0:
    if countdown <= 5:  # Dla ostatnich 5 sekund
        # Wyświetlenie liczby w słowach
        words = {5: "five", 4: "four", 3: "three", 2: "two", 1: "one"}
        print(words[countdown])
    else:
        print(countdown)  # Wyświetlenie liczby w formacie liczbowym
    countdown -= 1
    time.sleep(1)  # Czekanie 1 sekundy

print("Time's up!")
