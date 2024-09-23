def twoSum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i

nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(f"The indices of the two numbers that add up to {target} are: {result}")