def printer_error(s):
    count_error = 0
    for x in s:
        if x > 'm':
            count_error += 1
    return '{}/{}'.format(count_error, len(s))


if __name__ == '__main__':
    print(printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"))