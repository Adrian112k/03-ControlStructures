# Program sprawdzający prędkość samochodu na autostradzie

# Definiowanie minimalnej i maksymalnej dozwolonej prędkości
speed_limit_min = 40
speed_limit_max = 140

# Pobranie prędkości samochodu od użytkownika
car_speed = int(input("Enter car speed: "))

# Sprawdzenie, czy prędkość jest poza dozwolonym zakresem
if car_speed < speed_limit_min or car_speed > speed_limit_max:
    print("Warning: invalid car speed!!")
