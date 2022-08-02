import math


def is_square(n):
    if n < 0:
        return False
    elif round(math.sqrt(n), 2) * math.sqrt(n) == n:
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_square(16))
