# Program do znajdowania pierwszych N liczb pierwszych

# Pobranie liczby N od użytkownika
N = int(input("Enter the number of leading prime numbers to find: "))

# Lista do przechowywania liczb pierwszych
prime_numbers = []

# Liczba do sprawdzania, czy jest pierwsza
candidate = 2  # Zaczynamy od 2, ponieważ jest to pierwsza liczba pierwsza

# Dopóki nie znajdziemy N liczb pierwszych
while len(prime_numbers) < N:
    # Sprawdzenie, czy liczba jest pierwsza
    is_prime = True  # Zakładamy, że liczba jest pierwsza
    for i in range(2, int(candidate**0.5) + 1):  # Sprawdzamy dzielniki od 2 do sqrt(candidate)
        if candidate % i == 0:  # Jeśli znajdziemy dzielnik
            is_prime = False  # Liczba nie jest pierwsza
            break  # Przerywamy pętlę
    if is_prime:  # Jeśli liczba jest pierwsza
        prime_numbers.append(candidate)  # Dodajemy ją do listy liczb pierwszych
    candidate += 1  # Przechodzimy do kolejnej liczby

# Wyświetlenie wyników
print("Prime numbers:", *prime_numbers)
