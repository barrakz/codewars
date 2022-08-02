def accum(s):
    result = []
    for i, char in enumerate(s, 1):
        result.append((char * i).title())
    return '-'.join(result)

if __name__ == '__main__':
    print(accum("ZffdSffdIfd"))
