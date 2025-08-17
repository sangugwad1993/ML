def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True 

print(is_prime(21))

"""
21 < 2 <-- No, so continue to next step
range (2, int(21**0.5) + 1) = range(2, 5) = [2, 3, 4]
Check divisibility by 2
21 % 2 != 0 <-- No, so continue
Check divisibility by 3
21 % 3 == 0 <-- Yes, so returns False
 Check divisibility by 4
 The check for divisibility by 4 is never executed because the function returns immediately after finding 21 % 3 == 0.
 Final output: False
 Output: False
"""