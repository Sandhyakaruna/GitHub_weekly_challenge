def reverse_integer(x):
    sign = -1 if x < 0 else 1
    x = abs(x)
    reversed_x = int(str(x)[::-1]) * sign

    # 32-bit integer check
    if reversed_x < -2**31 or reversed_x > 2**31 - 1:
        return 0
    return reversed_x

# Example Usage
print(reverse_integer(123))   # Output: 321
print(reverse_integer(-456))  # Output: -654
print(reverse_integer(1534236469))  # Output: 0 (overflow case)
