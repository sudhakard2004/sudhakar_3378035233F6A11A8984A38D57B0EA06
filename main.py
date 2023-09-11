def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Example usage:
n = 5
print(f"The factorial of {n} is {factorial_recursive(n)}")
