# Sprawdzanie, czy zniżka jest dostępna
# Zniżka przysługuje dzieciom poniżej 18 roku życia
# lub osobom powyżej 65 roku życia.

age = int(input('Enter your age: '))

# Sprawdzamy, czy osoba jest uprawniona do zniżki
if age < 18 or age >= 65:
    print('You are eligible for a discount')
else:
    print('You are not eligible for a discount')
