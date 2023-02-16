def find_uniq(arr):
    new = []
    for i in arr:
        if i not in new:
            new.append(i)
    if arr.count(new[0]) > arr.count(new[1]):
        return new[1]
    else:
        return new[0]


def find_uniq_clever(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b


if __name__ == '__main__':
    print(find_uniq([1, 1, 1, 2, 1, 1]))
    print(find_uniq_clever([7, 7, 7, 7, 0.5, 7]))
