
n = 3
print(bin(n)[2:])

def int_to_bin(n, lst=None):
    if lst is None:
        lst = []
    while n > 1:
        for i in range(500,0,-1):
            x = 2 ** i
            p, q = divmod(n, x)
            if p == 0 and len(lst) > 0:
                lst.append(p)
            if p == 1:
                n -= n - q
                lst.append(p)
    lst.append(n)
    result = ''.join([str(x) for x in lst])
    return result

print(int_to_bin(n))