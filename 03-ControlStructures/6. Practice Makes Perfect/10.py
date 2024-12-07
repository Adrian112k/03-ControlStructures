# Program do obliczania wieku psa w latach psich

# Pobranie wieku psa w latach ludzkich
dog_age_in_human_years = int(input("Enter the dog's age in human years: "))

# Obliczanie wieku psa w latach psich
if dog_age_in_human_years <= 2:
    # Pierwsze dwa lata psa to 10,5 ludzkiego roku za każdy
    dog_age_in_dog_years = dog_age_in_human_years * 10.5
else:
    # Po dwóch latach, każdy rok psa to 4 lata ludzkie
    dog_age_in_dog_years = 2 * 10.5 + (dog_age_in_human_years - 2) * 4

# Wyświetlenie wyniku
print(f"The dog's age in dog's years is {dog_age_in_dog_years} years.")
