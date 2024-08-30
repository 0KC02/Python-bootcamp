import math

def calculate_rectangle_area():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is: {area}")

def calculate_circle_area():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * (radius ** 2)
    print(f"The area of the circle is: {area}")

def calculate_triangle_area():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is: {area}")

# Call the functions
calculate_rectangle_area()
print("")  # Add an empty line for spacing
calculate_circle_area()
print("")  # Add an empty line for spacing
calculate_triangle_area()

# Part 2
# Define the rectangle area calculation function
def calculate_rectangle_area(length, width):
    return length * width

# Define the circle area calculation function
def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

# Define the triangle area calculation function
def calculate_triangle_area(base, height):
    return 0.5 * base * height

# Define the square perimeter calculation function
def square_perimeter(side_length):
    return 4 * side_length

# Define the circle details function
def circle_details(radius):
    circumference = 2 * math.pi * radius
    area = calculate_circle_area(radius)
    print(f"The circumference of the circle is: {circumference}")
    print(f"The area of the circle is: {area}")

# Define the geometry function
def geometry(side_length, radius):
    square_perim = square_perimeter(side_length)
    circle_circumference = 2 * math.pi * radius
    square_area = side_length ** 2
    circle_area = calculate_circle_area(radius)

    if square_perim > circle_circumference:
        print("The square has a larger perimeter.")
    else:
        print("The circle has a larger circumference.")

    if square_area > circle_area:
        print("The square has a larger area.")
    else:
        print("The circle has a larger area.")

# Example usage
if __name__ == "__main__":
    # Example values
    length = 5
    width = 3
    base = 4
    height = 2
    side_length = 4
    radius = 3

    # Calculate areas
    print(f"Rectangle area: {calculate_rectangle_area(length, width)}")
    print(f"Triangle area: {calculate_triangle_area(base, height)}")

    # Circle details
    circle_details(radius)

    # Geometry comparison
    geometry(side_length, radius)
