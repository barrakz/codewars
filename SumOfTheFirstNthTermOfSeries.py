def series_sum(n):
    fractions = []
    for n in range(1, 3 * n - 1, 3):
        fractions.append(1 / n)
    return "{:.2f}".format(sum(fractions))


if __name__ == '__main__':
    print(series_sum(12))

'''
1 17 3
1 4 7 10 13 14
'''
