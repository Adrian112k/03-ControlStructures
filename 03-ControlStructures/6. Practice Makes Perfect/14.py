# Program sprawdzający, czy osoba jest dobrym influencerem

# Zmienne logiczne wskazujące, czy dana osoba ma konto na danym serwisie społecznościowym
facebook = True
twitter = False
instagram = True

# Sprawdzenie, czy osoba ma co najmniej dwa konta
accounts_count = 0

if facebook:
    accounts_count += 1
if twitter:
    accounts_count += 1
if instagram:
    accounts_count += 1

# Jeśli osoba ma co najmniej 2 konta, jest dobrym influencerem
if accounts_count >= 2:
    print("You are a good influencer!")
else:
    print("You are not a good influencer.")
