# Program do obliczania opłaty za parking
hours_parked = int(input("Enter the number of hours the car was parked: "))

if hours_parked >= 1 and hours_parked <= 2:
    fee = 5
elif hours_parked >= 3 and hours_parked <= 6:
    fee = 15
elif hours_parked > 6:
    fee = 20
else:
    fee = 0  # Jeśli liczba godzin jest mniejsza niż 1, nie nalicza się opłata

print(f"The parking fee for {hours_parked} hours is: {fee} PLN")
