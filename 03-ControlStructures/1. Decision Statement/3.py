# Sprawdzanie, czy samochód przekroczył dozwoloną prędkość

# Limit prędkości na autostradzie
speed_limit = 140  # Limit prędkości w km/h.

# Pobranie prędkości samochodu od użytkownika
car_speed = int(input('Enter car speed (km/h): '))  # Konwersja wejścia na liczbę całkowitą.

# Sprawdzenie, czy prędkość przekracza limit
if car_speed > speed_limit:  # Jeśli prędkość samochodu jest większa niż limit.
    print(f'Your speed is {car_speed} km/h')  # Wyświetlenie aktualnej prędkości.
    print('Warning: speed limit exceeded!!')  # Ostrzeżenie o przekroczeniu prędkości.
