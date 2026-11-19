
"""Practical 1: sum of squares in three styles."""

numbers = [3, 1, 4, 1, 5]

# 1. Imperative: step by step
result = 0
for n in numbers:
    result += n ** 2

print("imperative :", result)

# 2. Functional: combining functions
print("functional :", sum(map(lambda n: n ** 2, numbers)))

# 3. Declarative: stating what we want
print("declarative:", sum(n ** 2 for n in numbers))
