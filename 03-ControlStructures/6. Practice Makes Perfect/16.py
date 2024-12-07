# Oblicza całkowity czas prania
total_washing_time = 0

# Wybór programu prania
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ')

# Sprawdzamy, co użytkownik wybrał
if program == 'j':
    total_washing_time += 40  # Kurtka - 40 minut
elif program == 'u':
    total_washing_time += 70  # Bielizna - 70 minut
elif program == 's':
    total_washing_time += 20  # Buty - 20 minut
else:
    print('Invalid program selected!')
    exit()

# Sprawdzamy, czy wybrane jest dodatkowe płukanie
extra_rinse = input('Extra rinse? (y/n): ')
if extra_rinse == 'y':
    total_washing_time += 15  # Dodatkowe płukanie - 15 minut

# Sprawdzamy, czy wybrane jest dodatkowe wirowanie
extra_spin = input('Extra spin? (y/n): ')
if extra_spin == 'y':
    total_washing_time += 9  # Dodatkowe wirowanie - 9 minut

# Wyświetlamy całkowity czas prania
print(f'Total washing time: {total_washing_time} minutes')
