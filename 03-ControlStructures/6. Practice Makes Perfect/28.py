# Program do generowania pierwszych dwudziestu liczb Fibonacciego

# Inicjalizacja pierwszych dwóch liczb ciągu
fib1 = 0  # Pierwszy wyraz ciągu
fib2 = 1  # Drugi wyraz ciągu

# Wyświetlenie pierwszych dwóch liczb
print(fib1, fib2, end=' ')  # Wyświetlamy 0 i 1, oddzielając spacją

# Generowanie pozostałych 18 liczb
for _ in range(18):  # Pętla wykonuje się 18 razy
    next_fib = fib1 + fib2  # Obliczamy kolejną liczbę jako sumę dwóch poprzednich
    print(next_fib, end=' ')  # Wyświetlamy kolejną liczbę, oddzielając spacją
    fib1, fib2 = fib2, next_fib  # Aktualizujemy wartości fib1 i fib2
