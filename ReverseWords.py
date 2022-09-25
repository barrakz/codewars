def reverse_words(text):
    text_split = text.split(" ")
    print(text_split)
    result = []
    for x in text_split:
        result.append(x[::-1])

    return " ".join(result)


if __name__ == '__main__':
    print(reverse_words("This is it!"))
