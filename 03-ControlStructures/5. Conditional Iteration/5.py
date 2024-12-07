# Sums numbers entered by user and calculates their arithmetic mean
#
total_sum = 0  # Suma liczb
count = 0      # Licznik ilości wprowadzonych liczb

while True:
    # Pobieranie liczby od użytkownika
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Wyjście z pętli, gdy użytkownik wpisze 0
    
    # Dodanie liczby do sumy
    total_sum += number
    # Zwiększenie licznika liczb
    count += 1

# Wyświetlenie wyników
if count > 0:  # Sprawdzanie, czy wprowadzono jakiekolwiek liczby
    mean = total_sum / count  # Obliczanie średniej arytmetycznej
    print(f"The total sum of the numbers is: {total_sum}")
    print(f"The arithmetic mean of the numbers is: {mean}")
else:
    print("No numbers were entered.")
