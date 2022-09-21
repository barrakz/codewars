def filter_list(l):
    result = []
    for x in l:
        if type(x) == int:
            result.append(x)
    return result


if __name__ == '__main__':
    print(filter_list([1, 2, 'aasf', '1', '123', 123]))
