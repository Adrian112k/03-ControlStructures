# Program obliczający liczbę dni w miesiącu

# Pobranie numeru miesiąca od użytkownika
month = int(input('Enter month number (1..12): '))

# Sprawdzanie, ile dni ma dany miesiąc
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    days = 31  # Miesiące z 31 dniami
elif month == 4 or month == 6 or month == 9 or month == 11:
    days = 30  # Miesiące z 30 dniami
else:
    days = 28  # Luty zawsze ma 28 dni

# Wyświetlanie wyniku
print(f'Month {month} has {days} days')
