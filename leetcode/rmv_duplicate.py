def removeDuplicates(nums):
    if not nums:
        return 0

    # Initialize two pointers
    i = 0
    j = 1

    # Iterate through the array
    while j < len(nums):
        # If the current element is different from the previous one
        if nums[i] != nums[j]:
            # Move the pointer i one step forward and update the value at this position
            i += 1
            nums[i] = nums[j]
        # Move the pointer j one step forward
        j += 1

    # Return the number of unique elements
    return i + 1

# Original array
nums = [1, 2, 2, 3, 4, 4, 5]

# Call the removeDuplicates function
num_unique = removeDuplicates(nums)

# Print the number of unique elements
print("Number of unique elements:", num_unique)

# Print the updated array
print("Updated array:", nums[:num_unique])