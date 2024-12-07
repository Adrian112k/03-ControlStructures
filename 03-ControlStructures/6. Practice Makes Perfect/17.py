# Reads the time in 24-hour format
time_24 = input("Enter time (24-hour format): ")

# Splitting the input into hours and minutes
hours, minutes = map(int, time_24.split(":"))

# Determining AM or PM
if hours >= 12:
    period = "pm"
    if hours > 12:
        hours -= 12  # Convert hour to 12-hour format
else:
    period = "am"
    if hours == 0:
        hours = 12  # Midnight case (00:xx should be 12:xx am)

# Formatting the result in 12-hour format
time_12 = f"{hours}:{minutes:02d}{period}"

# Printing the result
print(f"Time in 12-hour format: {time_12}")
