# Program do generowania kuponu lotto (liczby od 1 do 49)

# Pętla do generowania wierszy
for i in range(1, 8):  # Liczby 1 do 7 (7 wierszy)
    for j in range(i, 50, 7):  # Liczby w każdej kolumnie (zaczynając od i, co 7)
        print(j, end=' ')  # Drukujemy liczbę
    print()  # Nowa linia po każdym wierszu
