import math


def find_next_square(sq):
    root = int(math.sqrt(sq))
    if root ** 2 == sq:
        return (root + 1) ** 2
    else:
        return -1


if __name__ == '__main__':
    print(find_next_square(121))
    print(find_next_square(625))
    print(find_next_square(65465))
