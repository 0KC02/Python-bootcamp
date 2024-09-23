def threeSum(nums):
    result = []
    freq = {}

    # Count the frequency of each number
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Sort the array
    nums.sort()

    # Iterate through the array
    for i in range(len(nums) - 2):
        # Skip duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Two pointers approach
        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                # Check for duplicates
                if (nums[i], nums[left], nums[right]) not in result:
                    result.append((nums[i], nums[left], nums[right]))

                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result

nums = [-1, 0, 1, 2, -1, -4]
result = threeSum(nums)
print(result)