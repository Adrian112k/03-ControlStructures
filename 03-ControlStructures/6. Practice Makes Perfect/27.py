for i in range(6, -1, -3):  # Pierwsza pętla iteruje przez liczby: 6, 3, 0
    for j in range(1, 4):   # Druga pętla iteruje przez liczby: 1, 2, 3
        print(f'{i+j}', end=' ')  # Drukuje sumę `i + j` w jednym wierszu, z odstępami
    print()  # Przechodzi do nowej linii po zakończeniu wewnętrznej pętli
