def elevator(left, right, call):
    if left - call == right - call:
        return "right"
    if call == left == right:
        return "right"
    if call == left:
        return "left"
    if call == right:
        return "right"
    if left > right and call == 2:
        return "left"
    if right > left and call == 0:
        return "left"
    else:
        return "right"


if __name__ == '__main__':
    print(elevator(0, 1, 1))
