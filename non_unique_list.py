def non_unique_list(lst):
    new_lst = []
    for elem in lst:
        if lst.count(elem) > 1:
            new_lst.append(elem)
    return new_lst
