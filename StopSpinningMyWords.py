def spin_words(sentence):
    result = []
    for x in sentence.split():
        if len(x) >= 5:
            result.append(x[::-1])
        else:
            result.append(x)
    return ' '.join(result)







if __name__ == '__main__':
    print(spin_words("Hey fellow warriors"))
