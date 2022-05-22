num = 12345
rev = 0
while (num != 0):
    lastDigit = num % 10
    rev = rev * 10 + lastDigit
    print(rev)
    num //= 10

print(num)
print("Hasil:")
print(rev)