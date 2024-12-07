# Oblicza sumę liczb całkowitych w zakresie <5, 10>

sum = 0

for i in range(5, 11):  # Zakres od 5 do 10 (11 jest wyłączone)
    sum += i  # Zamiast sum = sum + i używamy operatora +=

print(f'Sum is {sum}')
