###
# Walidator hasła
# Sprawdzanie, czy nowe hasło ma co najmniej 12 znaków
#
new_password = input('Enter new password: ')  # Pobieramy nowe hasło od użytkownika

# Sprawdzamy długość hasła
if len(new_password) < 12:  # Jeśli długość hasła jest mniejsza niż 12
    print('Password too short (min. 12 chars)')  # Wyświetlamy komunikat o za krótkim haśle
else:
    print('Password is valid')  # Jeśli hasło ma 12 lub więcej znaków, jest prawidłowe
