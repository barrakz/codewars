import math


def approx_equals(a, b):
    return math.isclose(a, b, abs_tol=0.001)


if __name__ == '__main__':
    print(approx_equals(175.9827, 82.25))
