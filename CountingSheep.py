def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i == True:
            count = count + 1
    return count


array1 = [True, True, True, False,
          True, True, True, True,
          True, False, True, False,
          True, False, False, True,
          True, True, True, True,
          False, False, True, True]

if __name__ == '__main__':
    print(count_sheeps(array1))
