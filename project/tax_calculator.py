def calculate_federal_tax(deducted_salary):
    federal_tax = 0
    previous_bracket_limit = 0
    for limit, rate in FEDERAL_TAX_BRACKETS:
        if deducted_salary > limit:
            federal_tax += (limit - previous_bracket_limit) * rate
            previous_bracket_limit = limit
        else:
            federal_tax += (deducted_salary - previous_bracket_limit) * rate
            break
    return federal_tax

def calculate_california_tax(deducted_salary):
    state_tax = 0
    previous_bracket_limit = 0
    for limit, rate in STATE_TAX_BRACKETS['California']:
        if deducted_salary > limit:
            state_tax += (limit - previous_bracket_limit) * rate
            previous_bracket_limit = limit
        else:
            state_tax += (deducted_salary - previous_bracket_limit) * rate
            break
    return state_tax

def calculate_new_york_tax(deducted_salary):
    state_tax = 0
    previous_bracket_limit = 0
    for limit, rate in STATE_TAX_BRACKETS['New York']:
        if deducted_salary > limit:
            state_tax += (limit - previous_bracket_limit) * rate
            previous_bracket_limit = limit
        else:
            state_tax += (deducted_salary - previous_bracket_limit) * rate
            break
    return state_tax

def calculate_fica(gross_salary):
    return gross_salary * 0.0765 if gross_salary <= 147000 else 147000 * 0.0765

def main():
    print("Welcome to the Net Salary Calculator!")
    print("This program calculates your net salary after federal, state, and FICA taxes.")
    
    # Constants
    FEDERAL_STANDARD_DEDUCTION = 13200
    STATE_STANDARD_DEDUCTION = {
        'California': 4609,
        'New York': 8000
    }
    global FEDERAL_TAX_BRACKETS
    FEDERAL_TAX_BRACKETS = [
        (11000, 0.10),
        (44725, 0.12),
        (95375, 0.22),
        (182100, 0.24),
        (231250, 0.32),
        (578125, 0.35),
        (float('inf'), 0.37)
    ]
    global STATE_TAX_BRACKETS
    STATE_TAX_BRACKETS = {
        'California': [
            (10099, 0.01),
            (23942, 0.02),
            (37788, 0.04),
            (52455, 0.06),
            (66295, 0.08),
            (338639, 0.093),
            (406364, 0.103),
            (677275, 0.113),
            (float('inf'), 0.123)
        ],
        'New York': [
            (8500, 0.04),
            (11700, 0.045),
            (13900, 0.0525),
            (80650, 0.0585),
            (215400, 0.0625),
            (1077550, 0.0685),
            (5000000, 0.0965),
            (25000000, 0.103),
            (float('inf'), 0.109)
        ]
    }
    
    # Getting User Input
    gross_salary = float(input("Please enter your gross salary: "))
    state = input("Please enter the state you reside in (California/New York): ")
    
    # Calculate Federal Tax
    deducted_salary = gross_salary - FEDERAL_STANDARD_DEDUCTION
    federal_tax = calculate_federal_tax(deducted_salary)
    
    # Calculate State Tax
    if state == 'California':
        state_deducted_salary = gross_salary - STATE_STANDARD_DEDUCTION['California']
        state_tax = calculate_california_tax(state_deducted_salary)
    elif state == 'New York':
        state_deducted_salary = gross_salary - STATE_STANDARD_DEDUCTION['New York']
        state_tax = calculate_new_york_tax(state_deducted_salary)
    else:
        print("State not supported.")
        return
    
    # Calculate FICA
    fica = calculate_fica(gross_salary)
    
    # Calculate Net Salary
    net_salary = gross_salary - federal_tax - state_tax - fica
    
    # Display Results
    print(f"\nGross Salary: ${gross_salary:.2f}")
    print(f"Federal Tax: ${federal_tax:.2f}")
    print(f"State Tax ({state}): ${state_tax:.2f}")
    print(f"FICA: ${fica:.2f}")
    print(f"Net Salary: ${net_salary:.2f}")

if __name__ == "__main__":
    main()
