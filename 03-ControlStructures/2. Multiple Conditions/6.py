# Program sprawdzający, czy liczba jest dodatnia, ujemna, czy równa zero.

# Pobranie liczby od użytkownika
number = int(input('Enter a number: '))

# Sprawdzenie, czy liczba jest dodatnia, ujemna, czy zero
if number > 0:
    print(f'Number {number} is positive')
elif number < 0:
    print(f'Number {number} is negative')
else:
    print('Number is 0')
