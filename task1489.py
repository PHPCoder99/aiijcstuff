A = int(input())

B = ""

isPrime = True
if A < 2:
    isPrime = False
else:
    for i in range(2, int(A ** 0.5) + 1):
        if A % i == 0:
            isPrime = False


for i in range(2, 10):
    while A % i == 0:
        B += str(i)
        A //= i

if isPrime or A != 1:
    print("Лимитированная партия")
elif B == "":
    print("1")
else:
    print(B)

# def t1489(A):
#     B = ""
#
#     isPrime = True
#     if A < 2:
#         isPrime = False
#     else:
#         for i in range(2, int(A ** 0.5) + 1):
#             if A % i == 0:
#                 isPrime = False
#
#     for i in range(2, 9):
#         while A % i == 0:
#             B += str(i)
#             A //= i
#
#     if isPrime:
#         return "x"
#     else:
#         return B
