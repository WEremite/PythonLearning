"""
    Copy only even numbers from list A to list B
    and square them.
"""

# Without comprehensions
A = [1, 2, 3, 4, 5, 7, 8, 12, 17, 21, 14, 5, 6, 2, 18]
B = []

for x in A:
    if x % 2 == 0:
        B.append(x ** 2)
print(B)

# With list comprehensions
C = [x ** 2 for x in A if x % 2 == 0]
print(C)
