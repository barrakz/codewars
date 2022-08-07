def alphabet_position(text):
    text = text.lower()
    string = ''

    for i in text:
        if i.isalpha():
            string += str(ord(i) - 96)
            string += ' '
    return string.rstrip()


if __name__ == '__main__':
    print(alphabet_position("The sunset sets at twelve o' clock."))


