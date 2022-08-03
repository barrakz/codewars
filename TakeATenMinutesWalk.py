def is_valid_walk(walk):
    ndirect = []
    sdirect = []
    wdirect = []
    edirect = []
    for x in walk:
        if x == 'n':
            ndirect.append(x)
    count_n = ndirect.count('n')

    for x in walk:
        if x == 's':
            sdirect.append(x)
    count_s = sdirect.count('s')

    for x in walk:
        if x == 'w':
            wdirect.append(x)
    count_w = wdirect.count('w')

    for x in walk:
        if x == 'e':
            edirect.append(x)
    count_e = edirect.count('e')

    if len(walk) != 10:
        return False
    else:
        if count_n != count_s or count_w != count_e:
            return False
        else:
            return True


def clever_walk_solution(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')


if __name__ == '__main__':
    print(is_valid_walk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))
    print(clever_walk_solution(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))
    print(clever_walk_solution(['n', 'w', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))
