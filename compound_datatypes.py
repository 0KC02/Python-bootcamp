# Create a list called fruits
fruits = ["apple", "banana", "cherry", "date"]

# Add "elderberry" to the end of the list
fruits.append("elderberry")

# Remove "banana" from the list
fruits.remove("banana")

# Sort the list in alphabetical order
fruits.sort()

# Print the list
print(fruits)

# Create a dictionary called student
student = {
    "name": "John Doe",
    "age": 25,
    "major": "Computer Science"
}

# Change the value of 'major' to "Electrical Engineering"
student["major"] = "Electrical Engineering"

# Add a new key-value pair: 'year' with a value of 'Senior'
student["year"] = "Senior"

# Print out the keys in the dictionary
print(student.keys())

# Print out the values in the dictionary
print(student.values())

# Create a list of dictionaries, where each dictionary represents a book
books = [
    {"title": "Book One", "author": "Author A", "year": 2001},
    {"title": "Book Two", "author": "Author B", "year": 2002},
    {"title": "Book Three", "author": "Author C", "year": 2003}
]

# Print the title of the second book in the list
print(books[1]["title"])

# Print the year the third book was published
print(books[2]["year"])

# Iterate over the list and print out each book's title and author
for book in books:
    print(f"Title: {book['title']}, Author: {book['author']}")

# Create a dictionary called courses
courses = {
    "math": ["Alice", "Bob", "Charlie"],
    "history": ["David", "Eve", "Frank"],
    "chemistry": ["Grace", "Heidi", "Ivan"]
}

# Add 5 students to "math"
courses["math"].extend(["Jack", "Kathy", "Liam", "Mona", "Nina"])

# Remove the third student from "history"
courses["history"].pop(2)

# Print out the students in "chemistry"
print(courses["chemistry"])

# Add a new course "physics" with a list of 4 students
courses["physics"] = ["Oscar", "Paul", "Quincy", "Rita"]

# Print the updated courses dictionary to verify changes
print(courses)
