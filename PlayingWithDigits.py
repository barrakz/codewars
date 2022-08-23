def dig_pow(n, p):
    result = 0
    for num in str(n):
        result += int(num) ** p
        p += 1

    if result % n == 0:
        return int(result / n)
    else:
        return -1


if __name__ == '__main__':
    print(dig_pow(46288, 3))
