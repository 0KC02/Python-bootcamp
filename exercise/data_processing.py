def main():
    # Task 1: Prompt the user to enter a sentence and then print the sentence in uppercase letters.
    sentence = input("Enter a sentence: ")
    print("Uppercase sentence:", sentence.upper())

    # Task 2: Prompt the user to enter a paragraph and then count the number of words in the paragraph.
    paragraph = input("Enter a paragraph: ")
    word_count = len(paragraph.split())
    print("Number of words in the paragraph:", word_count)

    # Task 3: Prompt the user for a string, and check if all the characters in the string are digits. Output true or false.
    string = input("Enter a string: ")
    print("All characters are digits:", string.isdigit())

    # Task 4: Prompt the user for a string, and replace all occurrences of the letter "a" with the letter "o".
    string_with_a = input("Enter a string: ")
    replaced_string = string_with_a.replace('a', 'o')
    print("String after replacing 'a' with 'o':", replaced_string)

    # Task 5: Prompt the user to enter their full name and then print their initials.
    full_name = input("Enter your full name: ")
    initials = ''.join([name[0].upper() for name in full_name.split()])
    print("Initials:", initials)

    # Task 6: Prompt the user for a string, then print its length.
    string_length = input("Enter a string: ")
    print("Length of the string:", len(string_length))

if __name__ == "__main__":
    main()
