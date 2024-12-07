# Program wypisujący nazwę uniwersytetu z dodatkowymi spacjami pomiędzy literami

university = 'Krakow University of Economics'  # Nazwa uniwersytetu
university_expanded = ''  # Zmienna, która będzie przechowywać nazwę z dodatkowymi spacjami

# Dodajemy spację pomiędzy każdą literą
for char in university:  # Dla każdej litery w nazwie uniwersytetu
    university_expanded = university_expanded + char + ' '  # Łączymy literę z przestrzenią

# Usuwamy ostatnią zbędną spację
university_expanded = university_expanded.strip()

# Wypisujemy oryginalną nazwę i nazwę z dodatkowymi spacjami
print(university)          # Oryginalna nazwa uniwersytetu
print(university_expanded) # Rozszerzona nazwa z spacjami
