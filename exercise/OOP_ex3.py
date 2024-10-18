# Base class Person
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def introduce(self):
        print(f"Hello, my name is {self.first_name} {self.last_name}")

# Subclass Employee that inherits from Person
class Employee(Person):
    def __init__(self, first_name, last_name, employee_id):
        # Call the constructor of the parent class Person
        super().__init__(first_name, last_name)
        self.employee_id = employee_id

    # Override the introduce method
    def introduce(self):
        print(f"Hello, my name is {self.first_name} {self.last_name}, and my employee ID is {self.employee_id}")

# Create an instance of the Person class
person = Person("John", "Doe")
person.introduce()  # Output: Hello, my name is John Doe

# Create an instance of the Employee class
employee = Employee("Jane", "Smith", "E12345")
employee.introduce()  # Output: Hello, my name is Jane Smith, and my employee ID is E12345

# Base class Shape
class Shape:
    def __init__(self, color):
        self.color = color

    def description(self):
        print(f"This shape is {self.color}")

# Subclass Square that inherits from Shape
class Square(Shape):
    def __init__(self, color, side_length):
        # Call the constructor of the parent class Shape
        super().__init__(color)
        self.side_length = side_length

    # Override the description method
    def description(self):
        print(f"This square is {self.color} and has a side length of {self.side_length}")

# Create an instance of the Shape class
shape = Shape("red")
shape.description()  # Output: This shape is red

# Create an instance of the Square class
square = Square("blue", 5)
square.description()  # Output: This square is blue and has a side length of 5

# Base class Vehicle
class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

    def drive(self):
        print("The vehicle is driving")

# Subclass Car that inherits from Vehicle
class Car(Vehicle):
    def __init__(self):
        # Call the constructor of the parent class Vehicle with 4 wheels
        super().__init__(4)

    # Override the drive method to accept an optional speed argument
    def drive(self, speed=None):
        if speed:
            print(f"The car is driving at {speed} mph")
        else:
            print("The car is driving")

# Create an instance of the Vehicle class
vehicle = Vehicle(2)
vehicle.drive()  # Output: The vehicle is driving

# Create an instance of the Car class
car = Car()
car.drive()          # Output: The car is driving
car.drive(60)        # Output: The car is driving at 60 mph

# Base class Rectangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Subclass Square that inherits from Rectangle
class Square(Rectangle):
    def __init__(self, side_length):
        # Call the constructor of the parent class Rectangle with both width and height as side_length
        super().__init__(side_length, side_length)

    def perimeter(self):
        return 4 * self.width  # or 4 * self.height (since they're equal in a square)

# Create an instance of the Rectangle class
rectangle = Rectangle(4, 6)
print(f"Rectangle area: {rectangle.area()}")  # Output: Rectangle area: 24

# Create an instance of the Square class
square = Square(5)
print(f"Square area: {square.area()}")         # Output: Square area: 25
print(f"Square perimeter: {square.perimeter()}")  # Output: Square perimeter: 20
