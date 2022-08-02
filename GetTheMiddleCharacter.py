def get_middle(s):
    even_first = int(len(s) / 2 - 1)
    even_second = int(len(s) / 2)
    odd_middle = int(len(s) / 2)

    if len(s) % 2 == 0:
        two_middles = s[even_first], s[even_second]
        return "".join(two_middles)
    else:
        return s[odd_middle]


if __name__ == '__main__':
    print(get_middle("testy"))
