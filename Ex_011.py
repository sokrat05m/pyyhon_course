# Как работает range

print(type(range(5)))
print(*range(6))
print(*range(2, 8, 2))
print(*range(5, 0, -1))
print(*range(2, 7))
from numpy import arange

print(arange(1, 5, 0.5))