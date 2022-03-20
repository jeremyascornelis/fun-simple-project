number = int(input())

#Pattern 1
for i in range(1, number):
    for j in range(1, number):
        print("*", end="")
    print()

print()

#Pattern 2
for i in range(1, number):
    for j in range(1, number):
        print(i, end="")
    print()

print()

#Pattern 3
for i in range(1, number):
    for j in range(1, number):
        print(j, end="")
    print()

print()

#Pattern 4
for i in reversed(range(1, number)):
    for j in reversed(range(1, number)):
        print(i, end="")
    print()

print()

#Another way for Pattern 4
"""
for i in range(5, 0, -1):
    for j in range(5, 0, -1):
        print(i, end="")
    print()
"""

#Pattern 5
for i in reversed(range(1, number)):
    for j in reversed(range(1, number)):
        print(j, end="")
    print()

print()

#Another way for Pattern 5
"""
for i in range(5, 0, -1):
    for j in range(5, 0, -1):
        print(j, end="")
    print()
"""