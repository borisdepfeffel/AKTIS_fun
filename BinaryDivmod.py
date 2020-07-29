# from random import randint


def int_to_bin(n, lst=None):
    # no need as passing anything but an empty list will break your implementation
    if lst is None:
        lst = []
    while n > 1:
        for i in range(500,0,-1):  # this is ruining the efficiency
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


def int_to_bin_v2(n):
    """ Similar but more efficient implementation """
    # Choice between a if statement here or removing any starting 0
    if n == 0:
        return '0'

    # get the closest 2^i > n
    power = 1
    while power <= n:
        power *= 2

    lst = []
    while power > 1:
        power //= 2
        p, n = divmod(n, power)
        lst.append(p)

    return ''.join([str(x) for x in lst])


def test_func(binary_calc_function):
    n = 0  # change this number for where to start test
    while True:
        # n = randint(0, 10000)  # can use random numbers to check, depends on what's best

        calc = binary_calc_function(n)
        # print(calc)

        # obviously this is the easiest way to get a bin str in python but what we are using
        # it for here is to force test our method - normally what you would do is use an 
        # inefficient but accurate method in order to test a more optimised one
        actual = str(bin(n))[2:]  # hope you looked up what the string split is doing

        if calc != actual:
            raise ValueError("Calculated: (%s) not equal to actual (%s) for %s" % calc, actual, n)

        if n > 10000:  # change this number for where to finish test
            break

        n += 1


if __name__ == '__main__':
    import timeit
    times_to_run = 1
    v1 = timeit.timeit("test_func(int_to_bin)", setup="from __main__ import test_func, int_to_bin", number=1)
    v2 = timeit.timeit("test_func(int_to_bin_v2)", setup="from __main__ import test_func, int_to_bin_v2", number=1)
    print(f"v1: {v1}\nv2: {v2}")
