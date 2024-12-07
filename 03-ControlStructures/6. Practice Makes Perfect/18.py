# Read the coordinates from the user
x = float(input("Enter the x coordinate: "))
y = float(input("Enter the y coordinate: "))

# Determine the location of the point
if x == 0 and y == 0:
    print(f"Point P({x},{y}) is at the origin of the coordinate system.")
elif x == 0:
    print(f"Point P({x},{y}) is on the y-axis.")
elif y == 0:
    print(f"Point P({x},{y}) is on the x-axis.")
elif x > 0 and y > 0:
    print(f"Point P({x},{y}) is in the first quadrant of the coordinate system.")
elif x < 0 and y > 0:
    print(f"Point P({x},{y}) is in the second quadrant of the coordinate system.")
elif x < 0 and y < 0:
    print(f"Point P({x},{y}) is in the third quadrant of the coordinate system.")
else:  # x > 0 and y < 0
    print(f"Point P({x},{y}) is in the fourth quadrant of the coordinate system.")