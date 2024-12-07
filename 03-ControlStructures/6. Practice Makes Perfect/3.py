###
# Oświetlenie w domu z trzema żarówkami i dwoma włącznikami
# Sprawdzanie, ile żarówek jest zapalonych
#
light_switch1 = False  # False - wyłączony włącznik, True - włączony włącznik
light_switch2 = False  # False - wyłączony włącznik, True - włączony włącznik
bulbs_on = 0  # Licznik zapalonych żarówek, początkowo 0

if light_switch1:  # Jeśli pierwszy włącznik jest włączony
    bulbs_on += 1  # Pierwszy włącznik zapala jedną żarówkę
if light_switch2:  # Jeśli drugi włącznik jest włączony
    bulbs_on += 2  # Drugi włącznik zapala dwie żarówki

print(f"Liczba zapalonych żarówek to: {bulbs_on}")  # Wyświetlenie liczby zapalonych żarówek
