# Program do obliczania całkowitego zużycia paliwa w zależności od trybu jazdy i odległości.

# Pobranie trybu jazdy od użytkownika
driving_mode = input('Enter driving mode (A/M/E): ').strip().upper()

# Pobranie odległości w kilometrach
distance = int(input('Enter distance in km: '))

# Sprawdzenie trybu jazdy i przypisanie odpowiedniego zużycia paliwa na 100 km
if driving_mode == 'A':
    fuel_consumption_per_100km = 7  # Tryb Auto (A) - 7 litrów na 100 km
elif driving_mode == 'M':
    fuel_consumption_per_100km = 9  # Tryb Manual (M) - 9 litrów na 100 km
elif driving_mode == 'E':
    fuel_consumption_per_100km = 6  # Tryb Eco (E) - 6 litrów na 100 km
else:
    print("Invalid driving mode entered.")
    exit()  # Kończymy działanie programu, jeśli wprowadzono niepoprawny tryb jazdy

# Obliczanie całkowitego zużycia paliwa
total_consumption = (fuel_consumption_per_100km * distance) / 100  # Zużycie paliwa w zależności od odległości

# Wyświetlanie wyników
print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption} liters')
