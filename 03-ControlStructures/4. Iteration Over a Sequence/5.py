# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position

plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # Sprawdzamy, czy znak to litera
    if char.isalpha():
        # Pobieramy kod znaku (używamy ord())
        char_code = ord(char)

        # Przesuwamy literę o jedno miejsce w prawo w alfabecie
        if char.islower():  # Dla liter małych
            char_code = ord(char) + 1
            if char_code > ord('z'):  # Jeśli przekroczy 'z', wracamy do 'a'
                char_code = ord('a')
        elif char.isupper():  # Dla liter dużych
            char_code = ord(char) + 1
            if char_code > ord('Z'):  # Jeśli przekroczy 'Z', wracamy do 'A'
                char_code = ord('A')

        # Zamieniamy kod nowego znaku na literę (używamy chr())
        encrypted_char = chr(char_code)

        # Dodajemy zaszyfrowany znak do zaszyfrowanego tekstu
        encrypted_text += encrypted_char
    else:
        # Jeśli znak nie jest literą (np. spacja, interpunkcja), dodajemy go bez zmian
        encrypted_text += char

# Wypisujemy oryginalny i zaszyfrowany tekst
print("Original text:", plain_text)
print("Encrypted text:", encrypted_text)
