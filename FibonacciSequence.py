
# seq = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
# Fn = Fn-1 + Fn-2
# F1 = 1
# F2 = 1.

def fib_num(n):
    sequence = [0, 1, 1]
    for num in range(n + 1):
        if num > 2:
            sequence.append(sequence[num-1] + sequence[num-2])
    return sequence[num]

print(fib_num(5))
