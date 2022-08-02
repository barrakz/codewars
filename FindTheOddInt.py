def find_it(seq):
    result = dict((i, seq.count(i)) for i in seq)
    for key, value in result.items():
        if value % 2 == 1:
            return key


if __name__ == '__main__':
    print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))
