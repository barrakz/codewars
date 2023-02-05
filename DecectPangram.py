import string


def is_pangram(s):
    alphabet = list(string.ascii_lowercase)
    output = ''
    sentence_lower = s.lower()

    for char in sentence_lower:
        if char.isalpha():
            output = output + char
    remove_duplicate = ''.join(set(output))

    for x in remove_duplicate:
        if x in alphabet:
            alphabet.remove(x)
    return alphabet == []


if __name__ == '__main__':
    print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
