cache = {0: 0, 1: 1}
x = input()

def fibonacci_of(n):
    if n in cache:  # Base case
        return cache[n]
    # Compute and cache the Fibonacci number
    cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case
    return cache[n]

for n in range(int(x)):
    print(fibonacci_of(n))
