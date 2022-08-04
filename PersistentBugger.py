def persistence(n):
    if n < 10:
        return 0
    total = 1
    for i in str(n):
        total = total * int(i)
    return 1 + persistence(total)


if __name__ == '__main__':
    print(persistence(39))
    print(persistence(999))
