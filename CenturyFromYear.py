def century(year):
    return int((year - 1) / 100) + 1


year = 400
print(century(year))
print(century(2022))