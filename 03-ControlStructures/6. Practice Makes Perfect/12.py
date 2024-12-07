# Program do obliczania kwoty do zapłaty z rabatem

# Wprowadzenie liczby zakupionych produktów i ceny produktu
number_of_products = int(input("Number of products purchased: "))
product_price = float(input("Product price: "))

# Obliczanie całkowitej ceny bez rabatu
total_price = number_of_products * product_price

# Jeśli zakupiono więcej niż 2 produkty, stosujemy rabat
if number_of_products > 2:
    total_price *= 0.75  # Zastosowanie 25% rabatu (0.75 to 75%)

# Wyświetlanie wyniku
print(f"Amount to pay: {total_price:.2f}")
