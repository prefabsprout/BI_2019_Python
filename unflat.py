test = [1, 1, 4, 4, 4, "hello", "hello", 4]


def unflat(lst):
    new_lst = []
    previous = lst[0]
    mini_lst = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] == previous:
            mini_lst.append(lst[i])
        if lst[i] != previous:
            new_lst.extend([mini_lst])
            mini_lst = [lst[i]]
        if i == len(lst) - 1:
            new_lst.extend([mini_lst])
        previous = lst[i]
    return new_lst


print(unflat(test))
