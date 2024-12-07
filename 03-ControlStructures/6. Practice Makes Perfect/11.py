# Program analizujący cenę produktu

# Wprowadzenie cen produktu
current_price = float(input("Current product price: "))
previous_price = float(input("Previous product price: "))

# Obliczanie procentowej zmiany ceny
price_reduction_percentage = ((previous_price - current_price) / previous_price) * 100

# Sprawdzanie, czy cena spadła o co najmniej 10%
if price_reduction_percentage >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {price_reduction_percentage:.0f}%")
else:
    print("No significant price reduction.")
