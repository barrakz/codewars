def digital_root(n):
    score = sum([int(num) for num in str(n)])
    if len(str(score)) > 1:
        score = digital_root(score)
    return score


if __name__ == '__main__':
    print(digital_root(5435342))

liczba = 432432

cos = str(map(iter, liczba))

print(cos)
