def order(sentence):
    list = []
    sentence = sentence.split()
    for i in range(1, len(sentence) + 1):
        for j in sentence:
            if str(i) in j:
                list.append(j)
    return " ".join(list)


def clever_order_solution(sentence):
    return ' '.join(sorted(sentence.split(), key=lambda w: sorted(w)))


if __name__ == '__main__':
    print(order("is2 Thi1s T4est 3a"))
    print(order("is2 Thi1s T4est 3a"))
