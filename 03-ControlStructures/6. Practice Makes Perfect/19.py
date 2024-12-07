# Survey program

# Asking the user the survey questions and saving their answers
interest_in_computer_science = input("Are you interested in computer science? (y/n): ") == 'y'
like_playing_computer_games = input("Do you like playing computer games? (y/n): ") == 'y'
has_instagram_account = input("Do you have an Instagram account? (y/n): ") == 'y'

# Printing the survey results
print("\nSURVEY RESULTS")
print(f"Interested in computer science: {'Yes' if interest_in_computer_science else 'No'}")
print(f"Playing computer games: {'Yes' if like_playing_computer_games else 'No'}")
print(f"Has an Instagram account: {'Yes' if has_instagram_account else 'No'}")
