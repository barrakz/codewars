def longest(a1, a2):
    a1 = set(a1)
    a2 = set(a2)

    combined = list(a1.union(a2))
    combined.sort()

    return ''.join(combined)


if __name__ == '__main__':
    print(longest("aretheyhere", "yestheyarehere"))
