def maskify(cc):
    if len(cc) > 4:
        count = len(cc)
        without_last_four = cc[0:count - 4]
        count_first_ch = len(without_last_four)
        result = cc.replace(without_last_four, count_first_ch * "#")
        return result
    else:
        return cc


def maskify_better(ccc):
    first_characters = len(ccc) - 4
    last_four = ccc[-4:]
    return '#' * first_characters + last_four


def mask_last_four_chars(s):
    if len(s) <= 4:
        return s
    else:
        return s[:-4] + "####"


if __name__ == '__main__':
    print(maskify('SF$SDfgsd2eA'))
    print(maskify_better('fffsdHJK898fsdfds9fsd'))
    print(mask_last_four_chars("fsfsd43r43fsdfgd54"))
    print(mask_last_four_chars("FRT"))
