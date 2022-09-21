def get_grade(s1, s2, s3):
    sum_average = (s1 + s2 + s3) / 3
    if sum_average > 90:
        return "A"
    if sum_average > 79 < 90:
        return "B"
    if sum_average > 69 < 80:
        return "C"
    if sum_average > 59 < 70:
        return "D"
    if sum_average > 49 < 60:
        return "F"
    else:
        return "F"


if __name__ == '__main__':
    print(get_grade(56, 87, 94))
