# Sprawdzanie, czy test został zaliczony
# Test jest zaliczony, gdy liczba poprawnie wykonanych zadań
# wynosi co najmniej 50%

# Liczba wszystkich zadań w teście
total_tasks = 20  # W teście było 20 zadań.

# Lista liczby poprawnie wykonanych zadań do przetestowania
tasks_ok_list = [20, 11, 10, 9, 0]  # Liczby poprawnych odpowiedzi.

# Pętla przechodząca przez każdą liczbę poprawnych odpowiedzi
for tasks_ok in tasks_ok_list:  # Iterujemy przez każdą wartość w liście 'tasks_ok_list'.
    print(f'Checking for {tasks_ok} correct tasks out of {total_tasks}.')  # Wyświetlamy aktualną liczbę poprawnych odpowiedzi.

    # Sprawdzenie, czy poprawnych odpowiedzi jest co najmniej 50%
    if tasks_ok >= total_tasks * 0.5:  # Jeśli liczba poprawnych odpowiedzi wynosi 50% lub więcej.
        test_passed = True  # Ustawiamy zmienną test_passed na True.
    else:
        test_passed = False  # Ustawiamy zmienną test_passed na False.

    # Wyświetlanie odpowiedniego komunikatu na podstawie wyniku
    if test_passed:
        print('Congratulations! You passed the test.')  # Jeśli test zaliczony.
    else:
        print('Unfortunately, you failed the test.')  # Jeśli test niezaliczony.

    print('---')  # Separator dla przejrzystości wyników.