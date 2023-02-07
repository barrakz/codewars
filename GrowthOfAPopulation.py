def nb_year(p0, percent, aug, p):
    year = 0
    temp = p0
    while temp < p:
        temp = int(temp * (percent / 100 + 1) + aug)
        year += 1
    return year


if __name__ == '__main__':
    print(nb_year(1500, 5, 100, 5000))
