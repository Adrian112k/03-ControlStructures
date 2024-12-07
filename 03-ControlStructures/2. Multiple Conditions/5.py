# Program do obliczania kwartału roku dla danego numeru miesiąca (1..12)

# Pobranie numeru miesiąca od użytkownika
month = int(input('Enter month number (1..12): '))

# Sprawdzanie, do którego kwartału należy dany miesiąc
if month >= 10:
    quarter = 4  # Miesiące 10, 11, 12 należą do czwartego kwartału
elif month >= 7:
    quarter = 3  # Miesiące 7, 8, 9 należą do trzeciego kwartału
elif month >= 4:
    quarter = 2  # Miesiące 4, 5, 6 należą do drugiego kwartału
else:
    quarter = 1  # Miesiące 1, 2, 3 należą do pierwszego kwartału

# Wyświetlanie wyniku
print(f'Month {month} is in quarter {quarter}')
