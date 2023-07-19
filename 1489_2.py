def find_unique_number(A):
    if A == 0:
        return 10  # Special case when A is 0, B will be 10.

    digits_B = []
    for factor in range(9, 1, -1):
        while A % factor == 0:
            digits_B.append(factor)
            A //= factor

    if A != 1:
        print("Лимитированная партия")
        return

    digits_B.sort()
    B = int(''.join(map(str, digits_B)))
    print(B)

find_unique_number(int(input()))
