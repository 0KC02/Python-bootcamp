class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

# Example usage:
rect = Rectangle(5, 3)
print(f"Area: {rect.get_area()}")
print(f"Perimeter: {rect.get_perimeter()}")

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hi, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")

# Example usage:
person = Person("Alice", 30, "female")
person.introduce()

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_genre(self):
        return self.genre

# Example usage:
book = Book("1984", "George Orwell", "Dystopian")
print(f"Title: {book.get_title()}")
print(f"Author: {book.get_author()}")
print(f"Genre: {book.get_genre()}")

class Student:
    def __init__(self, name, age, major, GPA):
        self.name = name
        self.age = age
        self.major = major
        self.GPA = GPA

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_major(self):
        return self.major

    def get_GPA(self):
        return self.GPA

    def calculate_grade(self):
        if self.GPA >= 3.7:
            return "A"
        elif self.GPA >= 3.0:
            return "B"
        elif self.GPA >= 2.0:
            return "C"
        else:
            return "F"

# Example usage:
student = Student("Bob", 20, "Computer Science", 3.5)
print(f"Name: {student.get_name()}")
print(f"Age: {student.get_age()}")
print(f"Major: {student.get_major()}")
print(f"GPA: {student.get_GPA()}")
print(f"Grade: {student.calculate_grade()}")

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def get_name(self):
        return self.name

    def get_species(self):
        return self.species

    def eat(self, food):
        print(f"{self.name} is eating {food}.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

# Example usage:
animal = Animal("Leo", "Lion")
print(f"Name: {animal.get_name()}")
print(f"Species: {animal.get_species()}")
animal.eat("meat")
animal.sleep()
