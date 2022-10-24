def find_short(s):
    len_list = []
    split_string = s.split()
    for word in split_string:
        len_list.append(len(word))
    return min(len_list)


if __name__ == '__main__':
    print(find_short("bitcoin take over the world maybe who knows perhaps"))
