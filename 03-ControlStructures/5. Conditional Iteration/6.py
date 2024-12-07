# Calculates the sum of even numbers from 1 to a given number N using a while loop
#
N = 10
sum_even = 0
i = 1  # Początkowy licznik

# Obliczanie sumy liczb parzystych za pomocą pętli while
while i <= N:
    if i % 2 == 0:  # Sprawdzanie, czy liczba jest parzysta
        sum_even += i  # Dodanie liczby parzystej do sumy
    i += 1  # Zwiększenie licznika

# Wyświetlenie wyniku
print(f"The sum of even numbers from 1 to {N} is: {sum_even}")
