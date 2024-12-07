# Pobieramy numer EAN-13 od użytkownika
ean_number = input('Enter EAN-13 article number: ')

# Sprawdzamy, czy numer ma dokładnie 13 znaków i składa się tylko z cyfr
if len(ean_number) == 13 and ean_number.isdigit():
    print('Article number is correct')
    
    # Sprawdzamy, czy pierwsze 3 cyfry to 590
    if ean_number.startswith('590'):
        print('Article manufactured in Poland')
else:
    print('Invalid EAN-13 number')
