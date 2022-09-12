def is_divisible(n,x,y):
    return n % x == 0 and n % y == 0


if __name__ == '__main__':
    print(is_divisible(12, 4, 3))
    print(is_divisible(13, 4, 3))