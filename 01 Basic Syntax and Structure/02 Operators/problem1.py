# Arithmetic Operators:
# Problem: Calculate the area and perimeter of a rectangle given its length and width.

# Input: Length and width of the rectangle
# Output: Area and perimeter of the rectangle

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate perimeter and area
area = length * width
perimeter = 2 * (length + width)

# Output the results
print("---------------------------")
print(f"Area of the Rectangle: {area}")
print(f"Perimeter of the Rectangle: {perimeter}")
print("---------------------------")

