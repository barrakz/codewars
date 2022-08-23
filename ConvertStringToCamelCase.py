def to_camel_case(text):
    text_replace = text.replace("-", " ").replace("_", " ")
    split_text = text_replace.split()

    if len(text) == 0:
        return text
    return split_text[0].title() + " ".join(split_text[1:]).title().replace(" ", "")




if __name__ == '__main__':
    print(to_camel_case("the_stealth_warrior"))



