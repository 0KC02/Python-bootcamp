class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2  # Diameter is twice the radius

# Create an instance of the Circle class
circle = Circle(5)

# Display the diameter
print(f"Diameter of the circle: {circle.diameter}")

class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("First name must be a non-empty string.")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Last name must be a non-empty string.")
        self._last_name = value

# Creating instances of the Person class
person = Person("John", "Doe")

# Getting the properties
print(f"First Name: {person.first_name}")  # Output: John
print(f"Last Name: {person.last_name}")    # Output: Doe

# Setting the properties to valid values
person.first_name = "Jane"
person.last_name = "Smith"

print(f"Updated First Name: {person.first_name}")  # Output: Jane
print(f"Updated Last Name: {person.last_name}")    # Output: Smith

# Testing the setter with invalid values
try:
    person.first_name = ""  # Should raise a ValueError
except ValueError as e:
    print(e)  # Output: First name must be a non-empty string.

try:
    person.last_name = None  # Should raise a ValueError
except ValueError as e:
    print(e)  # Output: Last name must be a non-empty string.

class Rectangle:
    def __init__(self, width, height):
        self.width = width  # This will call the setter for width
        self.height = height  # This will call the setter for height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be a positive number.")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be a positive number.")
        self._height = value

    @property
    def area(self):
        return self._width * self._height  # Calculate area

# Creating instances of the Rectangle class
try:
    rect = Rectangle(5, 10)

    # Getting properties
    print(f"Width: {rect.width}")  # Output: 5
    print(f"Height: {rect.height}")  # Output: 10
    print(f"Area: {rect.area}")  # Output: 50

    # Setting properties to valid values
    rect.width = 8
    rect.height = 12
    print(f"Updated Width: {rect.width}")  # Output: 8
    print(f"Updated Height: {rect.height}")  # Output: 12
    print(f"Updated Area: {rect.area}")  # Output: 96

    # Testing the setter with invalid values
    rect.width = -4  # Should raise a ValueError
except ValueError as e:
    print(e)  # Output: Width must be a positive number.

try:
    rect.height = 0  # Should raise a ValueError
except ValueError as e:
    print(e)  # Output: Height must be a positive number.

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self._balance = initial_balance  # Use a private variable for balance

    @property
    def balance(self):
        """Read-only property that returns the current balance."""
        return self._balance

    @property
    def is_overdrawn(self):
        """Read-only property that returns True if the account is overdrawn."""
        return self._balance < 0

    def deposit(self, amount):
        """Method to deposit money into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

    def withdraw(self, amount):
        """Method to withdraw money from the account."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount


# Example usage of the BankAccount class
account = BankAccount("123456789", 1000)

# Display initial balance and overdrawn status
print(f"Account Number: {account.account_number}")
print(f"Initial Balance: ${account.balance}")
print(f"Is Overdrawn: {account.is_overdrawn}")

# Perform some transactions
try:
    account.deposit(500)
    print(f"After depositing $500, balance: ${account.balance}")

    account.withdraw(200)
    print(f"After withdrawing $200, balance: ${account.balance}")

    account.withdraw(1500)  # This should raise an error due to insufficient funds
except ValueError as e:
    print(e)

# Final balance and overdrawn status
print(f"Final Balance: ${account.balance}")
print(f"Is Overdrawn: {account.is_overdrawn}")
