def max_product(nums):
    nums.sort()
    return max(nums[-1] * nums[-2], nums[0] * nums[1])  # Consider both positive and negative numbers

# Example Usage
print(max_product([3, 5, 1, 2, 4]))  # Output: 20 (5 * 4)
print(max_product([-10, -3, 5, 6, -2]))  # Output: 30 (-10 * -3)
print(max_product([-1, -2, -3, -4]))  # Output: 12 (-3 * -4)
