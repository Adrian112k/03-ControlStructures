# Prosty kalkulator
# Program pyta użytkownika o symbol operacji matematycznej (+, -, *, /)
# oraz dwie liczby. Program wykonuje odpowiednią operację matematyczną
# na tych liczbach i zwraca wynik.

# Pobranie dwóch liczb i symbolu operacji od użytkownika
number1 = float(input('Enter the first number: '))  # Pierwsza liczba
number2 = float(input('Enter the second number: '))  # Druga liczba
operator = input('Enter operator (+, -, *, /): ')  # Symbol operacji

# Wykonywanie odpowiedniej operacji na liczbach
if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    if number2 != 0:  # Sprawdzamy, czy nie dzielimy przez 0
        result = number1 / number2
    else:
        result = 'Error: Division by zero'
else:
    result = 'Invalid operator'

# Wyświetlanie wyniku
print(f'{number1} {operator} {number2} = {result}')
