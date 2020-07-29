
n = 450400493
print(bin(n)[2:])

def int_to_bin(n, lst=None):
    if lst is None:
        lst = []
    while n >= 0:
        if n == 1:
            lst.append(1)
            break
        elif n == 0:
            lst.append(0)
            break
        else:
            for i in range(500,0,-1):
                x = 2 ** i
                p, q = divmod(n, x)
                if p == 0 and len(lst) > 0:
                    lst.append(p)
                if p == 1:
                    n -= n - q
                    lst.append(p)
    result = ''.join([str(x) for x in lst])
    return result

print(int_to_bin(n))