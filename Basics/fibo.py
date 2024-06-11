"""module fibo handles Fibonacci sequence

Generate values by adding 2 previous ones, starting with 0, 1
Exemple: 0 1 1 2 3 5 8 13 21 34 ...
"""

n = 20

# Exercise 1: generate n elements of Fibonacci sequence and print them
a = 0
b = 1
for _ in range(n):
    c = a + b
    print(c, end=', ')
    a, b = b, c
print()

# Exercise 2: generate n elements of Fibonacci sequence and store them in a list
fibonacci_sequence = [0, 1]
for i in range(n-2):
    fibonacci_sequence.append(fibonacci_sequence[i] + fibonacci_sequence[i+1])
print(fibonacci_sequence)