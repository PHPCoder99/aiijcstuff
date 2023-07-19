A = int(input())

B = ""

isPrime = True
if A < 2:
    isPrime = False
else:
    for i in range(2, int(A ** 0.5) + 1):
        if A % i == 0:
            isPrime = False


for i in range(2, 9):
    while A % i == 0:
        B += str(i)
        A //= i

if isPrime:
    print("Лимитированная партия")
else:
    print(B)
