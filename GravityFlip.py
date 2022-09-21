def flip(d, a):
    if d == "R":
        return sorted(a)
    else:
        return sorted(a, reverse=True)


if __name__ == '__main__':
    print(flip("R", [3, 2, 1, 2]))
