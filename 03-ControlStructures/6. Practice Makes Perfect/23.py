# Program do generowania tabliczki mnożenia

# Pobranie liczby od użytkownika
number = int(input("Enter number: "))  # Wczytujemy liczbę od użytkownika i zamieniamy ją na typ całkowity (int)

# Pętla generująca tabliczkę mnożenia
for i in range(1, 11):  # Pętla iteruje przez liczby od 1 do 10 (range(1, 11) to zakres od 1 do 10 włącznie)
    result = number * i  # Obliczamy wynik mnożenia
    print(f"{number} x {i} = {result}")  # Wyświetlamy wynik w formacie: "liczba x mnożnik = wynik"
