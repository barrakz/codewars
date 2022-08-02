def find_outlier(integers):
    even = []
    odd = []
    for x in integers:

        if x % 2 == 0:
            even.append(x)
        else:

            odd.append(x)
    if len(even) == 1:
        return even[0]
    else:
        return odd[0]


if __name__ == '__main__':
    print(find_outlier([2, 4, 6, 8, 10, 3]))
