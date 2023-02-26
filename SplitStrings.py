def solution(s):
    if s == "":
        return []
    else:
        result = []
        i = 0
        while i < len(s):
            result.append(s[i:i + 2])
            i += 2
        if len(result[-1]) == 1:
            result[-1] += "_"
        return result


if __name__ == '__main__':
    print(solution("j"))
