def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)

# Example Usage
print(missing_number([3, 0, 1]))  # Output: 2
print(missing_number([0, 1]))  # Output: 2
print(missing_number([9,6,4,2,3,5,7,0,1]))  # Output: 8
