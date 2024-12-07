# Program wypisujący liczby od 1 do 30 z odpowiednimi zasadami

for num in range(1, 31):  # Pętla przechodząca przez liczby od 1 do 30
    output = ""  # Inicjalizacja pustego ciągu znaków, który przechowa wynik dla każdej liczby
    
    # Sprawdzamy, czy liczba jest podzielna przez 3 i/lub 5
    if num % 3 == 0:
        output += "THREE"
    if num % 5 == 0:
        output += " FIVE"
    
    # Jeśli liczba jest podzielna przez zarówno 3, jak i 5, wypisujemy 'BINGO'
    if num % 3 == 0 and num % 5 == 0:
        print("BINGO", end=" ")  # Wypisujemy 'BINGO' dla liczb podzielnych przez oba numery
    elif output:
        print(output.strip(), end=" ")  # Wypisujemy 'THREE' lub 'FIVE', jeśli liczba jest podzielna tylko przez jeden numer
    else:
        print(num, end=" ")  # Jeśli liczba nie jest podzielna przez 3 ani 5, wypisujemy liczbę
