def quarter_of(month):
    if month >= 10:
        return 4
    elif month >= 7:
        return 3
    elif month >= 4:
        return 2
    else:
        return 1


if __name__ == '__main__':
    print(quarter_of(8))
