def move_zeros(lst):
    zeros = []
    others = []

    for i in lst:
        if i == 0:
            zeros.append(i)
        else:
            others.append(i)
    return others + zeros


if __name__ == '__main__':
    print(move_zeros([1, 0, 1, 2, 0, 1, 3]))

