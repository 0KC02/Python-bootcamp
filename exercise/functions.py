# Function to replace every 's' with '$'
def dollarizer(word):
    return word.replace('s', '$')

# Function to replace every 'e' with '€'
def eurizer(word):
    return word.replace('e', '€')

# General function to replace character1 with character2
def replacer(word, char1, char2):
    return word.replace(char1, char2)

# Function to replace 's' with '$', 'e' with '€', and 'l' with '£'
def wonky_text(word):
    word = dollarizer(word)
    word = eurizer(word)
    word = replacer(word, 'l', '£')
    return word

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

# Function to calculate age in days
def age_in_days(age_years):
    return age_years * 365

# Function to calculate simple interest
def simple_interest(principal, rate, time):
    return principal * rate * time

# Function to check if the desired final amount is achieved
def plan_finances(principal, rate, time, desired_final_amount):
    final_amount = principal + simple_interest(principal, rate, time)
    return final_amount >= desired_final_amount

# Example usage
if __name__ == "__main__":
    print(dollarizer("success"))  # Output: $ucce$$
    print(eurizer("elephant"))    # Output: €l€phant
    print(replacer("hello", 'l', 'x'))  # Output: hexxo
    print(wonky_text("hello"))    # Output: h€££o
    print(celsius_to_fahrenheit(30))  # Output: 86.0
    print(age_in_days(25))  # Output: 9125
    print(simple_interest(1000, 0.05, 3))  # Output: 150.0
    print(plan_finances(1000, 0.05, 3, 1150))  # Output: True
