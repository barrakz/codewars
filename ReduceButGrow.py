def grow(arr):
    result = 1
    for i in arr:
        result = result * i
    return result


if __name__ == '__main__':
    print(grow([1,4,9]))