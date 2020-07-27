
lst = [[1, 9], 0, [23, 6], [8, [5, 9], [1, [1, 2]]]]

def list_check(x):
    if isinstance(x, list):
        return True
    return False

def iterate_list(x, new_lst):
    for item in x:
        if list_check(item):
            iterate_list(item, new_lst)
        else:
            new_lst.append(item)
    return new_lst


new_lst = []
iterate_list(lst, new_lst)
print(new_lst)