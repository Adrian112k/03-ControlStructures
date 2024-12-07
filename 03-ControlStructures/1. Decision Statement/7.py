# Program obliczający wynagrodzenie pracownika, uwzględniający premię.

# Podstawowe wynagrodzenie pracownika
basic_salary = 5000  # Wynagrodzenie bazowe w PLN.
total_salary = 0  # Całkowite wynagrodzenie (do obliczenia później).
bonus_percentage = 0.15  # Domyślna premia wynosi 15% wynagrodzenia bazowego.

# Sprawdzenie, czy pracownik otrzymuje premię
is_bonus = input('Does the employee receive a bonus? (Y/N): ').strip().upper() == 'Y'

# Obliczenie całkowitego wynagrodzenia
if is_bonus:
    bonus = basic_salary * bonus_percentage  # Obliczamy kwotę premii.
    total_salary = basic_salary + bonus  # Dodajemy premię do wynagrodzenia bazowego.
else:
    total_salary = basic_salary  # Jeśli nie ma premii, całkowite wynagrodzenie to wynagrodzenie bazowe.

# Wyświetlanie wyników
print(f'Basic salary: {basic_salary} PLN')  # Wynagrodzenie bazowe.
print(f'Bonus included? {"Yes" if is_bonus else "No"}')  # Czy premia została uwzględniona.
print(f'Total salary: {total_salary} PLN')  # Całkowite wynagrodzenie.
