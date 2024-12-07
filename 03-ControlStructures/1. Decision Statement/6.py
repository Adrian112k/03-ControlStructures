# Sprawdzanie, czy liczba wprowadzona z klawiatury jest parzysta czy nieparzysta

# Pobranie liczby od użytkownika
number = int(input('Enter number: '))  # Konwertujemy wejście na liczbę całkowitą.

# Sprawdzenie, czy liczba jest parzysta
if number % 2 == 0:  # Jeśli reszta z dzielenia liczby przez 2 wynosi 0, liczba jest parzysta.
    print(f'{number} is even')  # Wyświetlamy, że liczba jest parzysta.
else:
    print(f'{number} is odd')  # W przeciwnym razie wyświetlamy, że liczba jest nieparzysta.