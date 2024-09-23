class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if val not in nums:
            return len(nums)
        if len(nums) == 1 and val in nums:
            return 0
        idx = 0 
        j = len(nums) - 1
        while idx <= j:
            if nums[idx] == val:
                del nums[idx]
                j -= 1
            else:
                idx += 1
        return idx

# Example usage
nums = [3, 2, 2, 3]
val = 3
solution = Solution()
new_length = solution.removeElement(nums, val)
print(f"Updated list: {nums}")
print(f"New length: {new_length}")