def find_needle(haystack):
    for x in haystack:
        if x == 'needle':
            return (f"found the needle in position {haystack.index(x)}")


if __name__ == '__main__':
    print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))
