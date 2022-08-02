def count_bits(n):
    return list(bin(n)).count("1")


if __name__ == '__main__':
    print(count_bits(432423))
