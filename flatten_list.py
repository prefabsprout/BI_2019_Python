def flatten(lst):
    flat = []
    for i in lst:
        flat.append(i) if not isinstance(i, list) else flat.extend(i)
    return flat
