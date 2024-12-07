 #Program do sprawdzania rozmiarów odzieży

# Pobranie symbolu rozmiaru od użytkownika
size = input('Enter size symbol: ').strip().upper()  # Usuwamy spacje i zamieniamy na wielkie litery dla pewności.

# Sprawdzanie symbolu rozmiaru
if size == 'S':
    print('S: Small size')  # Rozmiar S - mały.
elif size == 'M':
    print('M: Medium size')  # Rozmiar M - średni.
elif size == 'L':
    print('L: Large size')  # Rozmiar L - duży.
elif size == 'XL':
    print('XL: Extra large size')  # Rozmiar XL - bardzo duży.
else:
    print('Incorrect symbol')  # Niepoprawny symbol.