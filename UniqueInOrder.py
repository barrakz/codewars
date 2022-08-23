def unique_in_order(iterable):
    result = []
    prev = None
    for i in iterable:
        if i != prev:
            result.append(i)
        prev = i
    return result


if __name__ == '__main__':
    print(unique_in_order('AAAABBBCCDAABBB'))
