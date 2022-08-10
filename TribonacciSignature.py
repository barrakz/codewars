def tribonacci(signature, n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))
    return signature[:n]


if __name__ == '__main__':
    print(tribonacci([0, 1, 1], 10))
