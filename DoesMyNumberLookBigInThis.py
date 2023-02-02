def narcissistic(value):
    num_str = str(value)
    length = len(num_str)
    total = 0
    for digit in num_str:
        total += int(digit) ** length
    return total == value



if __name__ == '__main__':
    print(narcissistic(371))
    print(narcissistic(4887))

