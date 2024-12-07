# Program do przekształcania podanej kwoty na jak najmniejszą liczbę monet (1 PLN, 2 PLN, 5 PLN)

# Wczytanie kwoty od użytkownika
amount = int(input("Enter the amount in PLN: "))

# Inicjalizacja liczby monet każdego typu
five_pln = 0
two_pln = 0
one_pln = 0

# Obliczanie liczby monet 5 PLN
five_pln = amount // 5
amount = amount % 5  # Pozostająca kwota po użyciu monet 5 PLN

# Obliczanie liczby monet 2 PLN
two_pln = amount // 2
amount = amount % 2  # Pozostająca kwota po użyciu monet 2 PLN

# Pozostała kwota to liczba monet 1 PLN
one_pln = amount

# Wyświetlenie wyniku
print(f"The amount of PLN {amount} in coins:")
print(f"5 PLN coins: {five_pln}")
print(f"2 PLN coins: {two_pln}")
print(f"1 PLN coins: {one_pln}")
