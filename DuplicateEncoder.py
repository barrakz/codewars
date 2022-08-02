def duplicate_encode(word):
    result = []
    word = word.lower()

    for letter in word:
        if word.count(letter) == 1:
            result.append('(')
        else:
            result.append(')')
    return ''.join(result)


if __name__ == '__main__':
    print(duplicate_encode("din"))
