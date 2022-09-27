def number(bus_stops):
    count_in = 0
    count_out = 0
    for stop in bus_stops:
        count_in += stop[0]
        count_out += stop[1]
    return count_in - count_out


if __name__ == '__main__':
    print(number([[10, 0], [3, 5], [5, 8]]))
