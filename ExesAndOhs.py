def xo(s):
    list_o = []
    list_x = []
    for x in s:
        if ("xo") not in s:
            return True
        if x.lower() == "x":
            list_x.append(x)
        if x.lower() == "o":
            list_o.append(x)
    return len(list_x) == len(list_o)


if __name__ == '__main__':
    print(xo("ooxXm"))
