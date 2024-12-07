# Terminal płatniczy
# Ustawienie początkowego stanu konta klienta
account_balance = 500  # Saldo konta wynosi 500 jednostek walutowych.

# Lista kwot do zapłacenia
payments = [140, 499, 500, 501, 720]  # Kwoty zakupów do przetestowania.

# Pętla przechodząca przez wszystkie kwoty zakupów
for total_payment in payments:  # Iterujemy przez każdą kwotę w liście 'payments'.
    print(f'Trying to pay {total_payment} units.')  # Wyświetlamy komunikat z aktualną kwotą do zapłaty.

    if total_payment <= account_balance:  # Sprawdzamy, czy saldo konta wystarcza na dokonanie płatności.
        print('Payment completed')  # Jeśli saldo jest wystarczające, drukujemy "Payment completed".
        account_balance -= total_payment  # Odejmujemy zapłaconą kwotę od salda konta.
    else:
        print('No funds')  # Jeśli saldo nie wystarcza, drukujemy "No funds".

    print(f'Current account balance: {account_balance}')  # Wyświetlamy aktualne saldo po każdej próbie płatności.
    print('---')  # Separator dla przejrzystości między transakcjami.