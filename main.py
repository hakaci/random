def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Enter nth fibonacci number
# It struggels after 35ty
# print(fibonacci(37))

def fibonacci_not_recursive(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

# Enter nth fibonacci number
# No wait time
print(fibonacci_not_recursive(1000))