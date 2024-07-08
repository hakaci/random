def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Enter nth fibonacci number
# It struggels after 35ty
print(fibonacci(37))