def factorial(n):
    if n == 0:
        return 1
    else:
        value = n * factorial(n - 1)
        print(n, value)
        return value

# Example usage
num = 3
result = factorial(num)
print(f"The factorial of {num} is {result}")