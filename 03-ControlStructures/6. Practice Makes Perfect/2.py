###
# Counts vowels in the text
#
text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0

# Index for while loop
index = 0

# Count vowels in the text using while
while index < len(text):  # Iterujemy przez każdy znak w tekście
    if text[index] in vowels:  # Sprawdzamy, czy znak jest samogłoską
        vowel_count += 1
    index += 1  # Przechodzimy do następnego znaku

print(f"The number of vowels in the text is: {vowel_count}")
