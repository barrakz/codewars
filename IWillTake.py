import math


def max_int_chain(n):
    if n < 5:
        return -1
    return math.floor(n / 2 + 1) * math.ceil(n / 2 - 1)


if __name__ == '__main__':
    print(max_int_chain(39))
