# Program do sprawdzania kodu PIN

# Ustawienie poprawnego kodu PIN
correct_pin = "0805"  # Poprawny kod PIN
attempts = 3  # Maksymalna liczba prób

# Pętla do wprowadzania kodu PIN przez użytkownika
while attempts > 0:  # Dopóki użytkownik ma próby
    entered_pin = input("Enter the PIN code: ")  # Pobieramy kod PIN od użytkownika
    
    if entered_pin == correct_pin:  # Sprawdzamy, czy wprowadzony kod jest poprawny
        print("Correct!")
        break  # Wyjście z pętli, jeśli kod jest poprawny
    else:
        attempts -= 1  # Zmniejszamy liczbę pozostałych prób
        print("Incorrect...")  # Informujemy o błędzie
    
    if attempts == 0:  # Jeśli użytkownik zużył wszystkie próby
        print("Sorry, your payment card has been blocked.")  # Blokada karty
