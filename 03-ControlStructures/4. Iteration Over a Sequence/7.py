# Oblicza sumę liczb parzystych w zakresie <1, 10>

sum = 0

for i in range(1, 11):  # Zakres od 1 do 10 (11 jest wyłączone)
    if i % 2 != 0:  # Sprawdzamy, czy liczba nie jest parzysta
        continue  # Jeśli liczba nie jest parzysta, pomijamy ją
    sum += i  # Dodajemy liczbę parzystą do sumy

print(f'Sum of even numbers in the range <1,10> is {sum}')
