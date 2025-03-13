def remove_duplicates(nums):
    if not nums:
        return 0

    index = 1  # Pointer for unique elements
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[index] = nums[i]
            index += 1

    return index

# Example Usage
arr = [1, 1, 2, 2, 3, 4, 4, 5]
length = remove_duplicates(arr)
print(arr[:length])  # Output: [1, 2, 3, 4, 5]
