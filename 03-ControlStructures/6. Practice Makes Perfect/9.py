# Program sprawdzający, czy imię jest żeńskie (kończy się na literę "a")

# Pobranie imienia od użytkownika
name = input('Enter name: ')

# Sprawdzenie, czy imię kończy się na literę "a"
if name.endswith('a'):
    print(f'{name} -- Polish female name')
else:
    print(f'{name} -- Not a Polish female name')
