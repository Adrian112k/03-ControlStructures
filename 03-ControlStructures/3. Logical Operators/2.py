# Sprawdzanie loginu i hasła

# Zdefiniowane poprawne login i hasło
login = 'joe'
password = 'abcd'

# Pobranie loginu i hasła od użytkownika
entered_login = input('Login: ')
entered_password = input('Password: ')

# Sprawdzanie, czy wprowadzony login i hasło są poprawne
if login == entered_login and password == entered_password:
    print('You are logged in')
else:
    print('Incorrect login or password!!')
