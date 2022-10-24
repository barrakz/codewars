def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    temp_kelvin = 273.15 + temp
    num = ((given_mass1 / molar_mass1 + given_mass2 / molar_mass2) * 0.082 * temp_kelvin)
    return num / volume



if __name__ == '__main__':
    print(solution(44, 30, 3, 2, 5, 50))
