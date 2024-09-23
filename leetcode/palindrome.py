def is_palindrome(x: int) -> bool:
    # If x is negative, it cannot be a palindrome
    if x < 0:
        return False

    # Convert x to string and compare it with its reverse
    return str(x) == str(x)[::-1]

number = 12321
result = is_palindrome(number)
print(result)