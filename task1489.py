A = int(input())

B = ""

for i in reversed(range(1, 10)):
    while A % i == 0:
        B += str(i)
        A //= i

B = "".join(sorted(list(B)))

if A != 1:
    print("Лимитированная партия")
elif B == "":
    print("1")
else:
    print(B)
