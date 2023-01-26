def get_sum(a, b):
    if a == b:
        return a
    elif a < b:
        return sum(range(a, b+1))
    else:
        return sum(range(b, a+1))


if __name__ == '__main__':
    print(get_sum(0, -1))
    print(get_sum(-1, 2))
    print(get_sum(-10, 4))
    print(get_sum(4, -5))
    print(get_sum(1, 5))