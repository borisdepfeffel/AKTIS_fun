
print(bin(1))
print(bin(2))
print(bin(3))

number = 500

def integer_to_bin(n):
    lst = []
    for i in range(10, -1, -1):
        if 2 ** i <= n:
            n -= 2 ** i
            for num in range(i + 1):
                if i + 1 >= len(lst):
                    lst.append(0)
            lst[i] = 1
    lst = list(reversed(lst))

    for num in lst:
        print(num, end='')


integer_to_bin(460)
