
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

# Very clean.Like the use of list_check as proof of concept even though it doesn't add much.
# Harder version would be to try with iteration.
# Good using isinstance rather than type() == list.

def iterate_list(x, new_lst=None):
    """
    Rather than having to pass in a list, this uses None as a default arg and assigns
    a new list if not passed. Don't use [] or {} as default args though as they're mutable!
    """
    if new_lst is None:
        new_lst = []
    for item in x:
        if isinstance(item, list):
            iterate_list(item, new_lst)
        else:
            new_lst.append(item)
    return new_lst


flat_list = iterate_list(lst, new_lst)
print(flat_list)
