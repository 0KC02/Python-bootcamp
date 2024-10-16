def custom_len(input_list):
    count = 0
    for _ in input_list:
        count += 1
    return count

def custom_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def custom_min(numbers):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest

def custom_max(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

def custom_sorted(input_list, reverse=False):
    sorted_list = []
    while input_list:
        smallest = input_list[0]
        for num in input_list:
            if num < smallest:
                smallest = num
        sorted_list.append(smallest)
        input_list.remove(smallest)
    if reverse:
        sorted_list.reverse()
    return sorted_list

def custom_reversed(input_list):
    reversed_list = []
    for i in range(len(input_list)-1, -1, -1):
        reversed_list.append(input_list[i])
    return reversed_list