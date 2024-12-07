# Sprawdzenie, czy przynajmniej jedna z liczb nie jest ujemna

# Pobranie dwóch liczb od użytkownika
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

# Sprawdzanie, czy przynajmniej jedna liczba nie jest ujemna
if not x < 0 or not y < 0:
    print(f'At least one of the numbers {x} and {y} is not negative')
else:
    print('Both numbers are negative')
