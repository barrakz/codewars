def create_phone_number(n):
    numbers_str = "".join([str(x) for x in n])
    return str("(" + numbers_str[0:3] + ")" + " " + numbers_str[3:6] + "-" + numbers_str[6::])


if __name__ == '__main__':
    print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
